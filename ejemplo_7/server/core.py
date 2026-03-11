"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       10/03/2026
    Comments:   Basic example using router
"""
import logging
import sys
import uvicorn
from fastapi import FastAPI

logger = logging.getLogger("Server Core")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(name)s - %(message)s'))
logger.addHandler(console_handler)

HOST = "localhost"
PORT = 8300
RECOMMENDS = """
    - Accede a http://localhost:8300/public/ para probar el endpoint
    - Revisa el ejemplo 5 antes!!.
    - Para verificar si se agregan cabeceras en la respuesta, una forma simple de verificarlo es 
        acceder a las herramientas de desarrollo del navegador (generalmente con F12), y dentro
        de 'Network' seleccionar la petición realizada y revisar las cabeceras de la respuesta 
        (Response Headers).
    - Accede a http://localhost:8300/public/avoid para ver como saltear un middleware.
    
"""

app=  FastAPI(title= "Server Core")

def run_server():
    uvicorn.run(f"{__name__}:app", host=HOST, port=PORT, reload=True)
