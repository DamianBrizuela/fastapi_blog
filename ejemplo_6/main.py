"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       8/1/2025
    Comments:   Basic usage of middlewares
"""

import uvicorn
from fastapi import FastAPI
from endpoints.public_router import public_router_tag
from middleware import CustomHeaderMiddleware, time_mesurement, BaseHTTPMiddleware

HOST = "localhost"
PORT = 8300
RECOMMENDS = """
    - Accede a http://localhost:8300/public/ para probar el endpoint
    - Revisa el ejemplo 5 antes!!.
    - Para verificar si se agregan cabeceras en la respuesta, una forma simple de verificarlo es 
        acceder a las herramientas de desarrollo del navegador (generalmente con F12), y dentro
        de 'Network' seleccionar la petición realizada y revisar las cabeceras de la respuesta 
        (Response Headers).
    - Accede a http://localhost:8300/public/avoid para ver como saltear un middleware
    
"""

app= FastAPI(title= "FastApi")
app.add_middleware(BaseHTTPMiddleware, dispatch= time_mesurement)
app.add_middleware(CustomHeaderMiddleware, comments="Esto es solo un comentario por ahora!")

app.include_router(public_router_tag)

def init_server():
    print(f"FastAPI Server running on url: {HOST}:{PORT}   ...\n")
    print("example 6 -> middleware \n")
    print(f"Modo de uso: {RECOMMENDS} \n")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)

if __name__ == "__main__":
    init_server()
    # accede a http://localhost:8300/public/welcome para probar el endpoint
