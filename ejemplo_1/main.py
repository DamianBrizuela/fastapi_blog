"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       25/11/2025
    Comments:   Basic example for using FastApi
"""

import uvicorn
from fastapi import FastAPI

HOST = "localhost"
PORT = 8300

app= FastAPI(title= "FastApi")

# enrutamiento básico
# usando GET para definir un endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World from example 1!"}

# enrutamiento con POST (se puede comprobar mediante un curl o postman)
"""
    curl -X POST http://127.0.0.1:8000/info \
     -H "Content-Type: application/json"
 """
@app.post("/info")
def get_status():
    return {"message": "ok- using POST verb"}


def init_server():
    print(f"FastAPI Server running on url: {HOST}:{PORT}   ...\n")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)

if __name__ == "__main__":
    init_server()
