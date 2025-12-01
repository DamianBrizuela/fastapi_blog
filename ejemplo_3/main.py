"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       28/11/2025
    Comments:   Basic example using routers and Http responses
"""

import uvicorn
from fastapi import FastAPI
from endpoints import *

HOST = "localhost"
PORT = 8300

app= FastAPI(title= "FastApi")

# incluyo en FastAPI un router
# Me permitira ordenar mis endpoints
app.include_router(public_router_tag)

def init_server():
    print(f"FastAPI Server running on url: {HOST}:{PORT}   ...\n")
    print("example 3 -> routers & HTTP \n")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)

if __name__ == "__main__":
    init_server()
    # accede a http://localhost:8300/public/welcome para probar el endpoint
