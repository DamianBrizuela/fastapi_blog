"""
    Author:     Damian Brizuela
    version:    1.1.0
    Date:       28/11/2025
    Comments:   Basic module for using FastApi routers - step 3
"""

import uvicorn
from fastapi import FastAPI
from step_3.routers import first_router

HOST = "localhost"
PORT = 8301

app= FastAPI(title= "FastApi")

# step 1 enrutamiento básico
@app.get("/")
def read_root():
    return {"message": "Hello World from step 1!"}

@app.get("/status")
def get_status():
        return {"message": "ok-step-2"}
    
# step 2 enrutamiento con POST (se puede comprobar mediante un curl o postman)
"""
    curl -X POST http://127.0.0.1:8000/info \
     -H "Content-Type: application/json"
 """
@app.post("/info")
def get_status():
    return {"message": "ok-step-2 POST verb"}

# step 3 usando routers (agrupando endpoints)


def init_server():
    print(f"FastAPI Server running on url: {HOST}:{PORT}   ...\n")
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)

if __name__ == "__main__":
    init_server()
