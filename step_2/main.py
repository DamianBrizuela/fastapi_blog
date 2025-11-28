"""
    Author:     Damian Brizuela
    version:    1.0.1
    Date:       28/11/2025
    Comments:   Basic module for using FastApi adding endpoints - step 2
"""

import uvicorn
from fastapi import FastAPI

HOST = "localhost"
PORT = 8300

app= FastAPI(title= "FastApi")

@app.get("/")
def root():
    return {"message": "ok-fastapi"}

@app.get("/other-endpoint")
def root2():
    return {
        "message": "ok",
        "response": "this is another endpoint"
    }

@app.post("/post-endpoint")
def root3():
    return {
        "message": "ok-post",
        "response": "this is another post endpoint"
    }

def init_server():
    uvicorn.run("main:app", host=HOST, port=PORT, reload=False)
    print("FastAPI Server running...")


if __name__ == "__main__":
    init_server()
