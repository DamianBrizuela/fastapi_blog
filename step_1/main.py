"""
    Author:     Damian Brizuela
    version:    1.1.0
    Date:       28/11/2025
    Comments:   Basic module for using FastApi routers - step 3
"""

import uvicorn
from fastapi import FastAPI

HOST = "localhost"
PORT = 8300

app= FastAPI(title= "FastApi")

@app.get("/")
def root():
    return {"message": "ok-fastapi"}

def init_server():

    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
    print("FastAPI Server running...")


if __name__ == "__main__":
    init_server()
