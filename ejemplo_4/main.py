"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       02/12/2025
    Comments:   Basic example using endpoint with api-key security
"""

import uvicorn
from fastapi import FastAPI
from endpoints import *

HOST = "localhost"
PORT = 8300

app= FastAPI(title= "FastApi")

app.include_router(secure_router)

def init_server():
    print(f"FastAPI Server running on url: {HOST}:{PORT}   ...\n")
    print("example 4 -> routers with API-Key \n")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)

if __name__ == "__main__":
    init_server()
    # accede a http://localhost:8300/public/welcome para probar el endpoint
