"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       28/11/2025
    Comments:   example 4. Router using a API-Key security
"""

from fastapi import APIRouter, HTTPException
from models_request import data
from secure_apikey.verify_apikey import validar_api_key

secure_router = APIRouter(prefix= '/api', tags=["Secure endpoints"])
# defino un prefijo 'public' en la url

@secure_router.get("/status")
def status():
    print("insecure endpoint called")
    return {"message": "No necesitas acceder con api-key este endpoint"}

# Ejemplo de curl para probarlo si no tienes o usas postman o no quieres usar el docs de Fastapi
"""
    curl -L -X POST 'localhost:8300/api/sensible-info' \
        -H 'Content-Type: application/json' \
        -H 'api-key: secreto-oterces' \
        -d '{
            "str_data":"texto basico",
            "some_number":1
        }'
"""
@secure_router.post("/sensible-info")
def secure_endpoint(values: data):

    print("secure 'sensible info' endpoint called")
    response = f"Has enviado el string: {values.str_data} y el número: {values.some_number}"
    return {'result': response}

@secure_router.post("/other-endpoint")
def other_endpoint(values: data):

    print("secure 'other secure' endpoint called")
    if values.some_number >= 5:
        response = f"Has enviado el string: {values.str_data}, prueba enviar un número menor a 5"
        return {'result': response}
    
    # lanzamos un error si el primer valor es menor que el segundo, a modo de prueba
    return HTTPException(
        status_code= 400,
        detail= "Deberias enviar un número mayor o igual a 5."
    )