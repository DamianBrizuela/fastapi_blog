"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       10/03/2026
    Comments:   Basic example using router
"""

from server import ServerCore
import logging
logger = logging.getLogger("Main")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(name)s - %(message)s'))
logger.addHandler(console_handler)

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

if __name__ == "__main__":
    logger.info("example 7 -> externalization \n")
    logger.debug(f"Modo de uso: {RECOMMENDS} \n")
    
    server = ServerCore(HOST, PORT)
    server.run()
