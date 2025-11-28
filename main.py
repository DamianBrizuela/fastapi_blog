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
PORT = 8300

app= FastAPI(title= "FastApi")
app.include_router(first_router)

def init_server():

    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
    print("FastAPI Server running...")


if __name__ == "__main__":
    init_server()
