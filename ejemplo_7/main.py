"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       10/03/2026
    Comments:   Basic example using router
"""

from server import run_server

HOST = "localhost"
PORT = 8300
RECOMMENDS = """
    - Accede a http://localhost:8300/docs para probar el endpoint
    - Integración del servidor como una clase.
    - Para verificar si se agregan cabeceras en la respuesta, una forma simple de verificarlo es 
        acceder a las herramientas de desarrollo del navegador (generalmente con F12), y dentro
        de 'Network' seleccionar la petición realizada y revisar las cabeceras de la respuesta 
        (Response Headers).
    
"""


def init_server():
    
    run_server()
    print("example 7 -> externalization \n")
    print(f"Modo de uso: {RECOMMENDS} \n")

    

if __name__ == "__main__":
    init_server()
    # accede a http://localhost:8300/docs para probar el endpoint
