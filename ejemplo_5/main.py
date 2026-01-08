"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       8/1/2025
    Comments:   Basic usage of middlewares
"""

import uvicorn
from fastapi import FastAPI
from endpoints.public_router import public_router_tag
from middleware import time_mesurement, BaseHTTPMiddleware

HOST = "localhost"
PORT = 8300
RECOMMENDS = """
    - Accede a http://localhost:8300/public/ para probar el endpoint
    - Si accedes a otra url, podras ver los datos propocionados, ya que los middleware acceden a los
        datos de la peticion y respuesta.
    - Prueba acceder a alguna ruta definida que contenga /manteinance/ o /private/ para ver como los 
        middlewares bloquean el acceso con un mensaje particular

"""

app= FastAPI(title= "FastApi")
app.add_middleware(BaseHTTPMiddleware, dispatch= time_mesurement)

app.include_router(public_router_tag)

def init_server():
    print(f"FastAPI Server running on url: {HOST}:{PORT}   ...\n")
    print("example 5 -> middleware \n")
    print(f"Modo de uso: {RECOMMENDS} \n")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)

if __name__ == "__main__":
    init_server()
    # accede a http://localhost:8300/public/welcome para probar el endpoint
