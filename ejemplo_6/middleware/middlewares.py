"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       8/1/2025
    Comments:   Middlewares examples -
        Debo importar desde el __init_.py BaseHTTPMiddleware para luego desde el main.copy()
        hacer uso del middleware que defino aqui. Podria simplemente dejarse todo dentro del main, 
        pero perderia la capacidad de modularizar el codigo.
"""

from fastapi import Request
from fastapi.responses import JSONResponse
import time

async def time_mesurement(request: Request, call_next):

    def check_path(path: str):
        blocked_paths = ["private", "manteinance"]
        for blocked in blocked_paths:
            if blocked in path:
                return True
        return False

    if check_path(request.url.path):
        return JSONResponse(
            status_code=503,
            content={"message": "El servicio solicitado está temporalmente fuera de servicio por mantenimiento."}
        )

    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time

    response.headers["X-Process-Time"] = str(process_time)
    print(f"Procesando la peticion {request.url} en: {process_time} segundos")
    return response