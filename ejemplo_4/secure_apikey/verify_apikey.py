"""
funcion para verificar si el apikey es correcta y el router permite el accesso
a un endpoint definido
"""

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

# apikey que NO VA DEFINIDA ASI!!! es solo un ejemplo!!!, lo ideal es que este en un .env
# o de manera que no pueda accederse facilmente.add()
API_KEY = "secreto-oterces"
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

def validar_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API key inválida")
    return api_key