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

""" Emojis
🟨​🟩​🟦​🟥​🟧​⬜​🔴​🟠​🟡​🟢​🔵​🟣​🟤​⚫​⚪
"""

app=  FastAPI(title= "FastAPI Core")

class ServerCore:

    def __init__(self, host, port):
        self.host= host
        self.port= port
        self.running= False
        logger.debug(f"🟧 Set server at {host}:{port}")

    def run(self):
        uvicorn.run(
            f"{__name__}:app", 
            host= self.host, 
            port= self.port,
            reload=True
        )
        self.running = True
        logger.debug(f"🟩 Server Running")