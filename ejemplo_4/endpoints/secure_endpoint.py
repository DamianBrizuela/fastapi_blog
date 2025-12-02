"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       28/11/2025
    Comments:   example 4. Router using a API-Key security
"""

from fastapi import APIRouter, HTTPException
from models_request import data

secure_router = APIRouter(prefix= '/calc', tags=["Secure endpoints"])
# defino un prefijo 'public' en la url

@secure_router.get("/status")
def status():
    print("insecure endpoint called")
    return {"message": "No necesitas acceder con api-key este endpoint"}

@secure_router.post("/sensible-info")
def secure_endpoint(values: data):

    print("insecure endpoint called")
    result = f'{values.first_number + values.second_number}'
    return {'result': result}

@secure_router.post("/other-endpoint")
def other_endpoint(values: data):

    if (values.first_number >= values.second_number):
        return {"result": f"{values.first_number - values.second_number}"}
    
    # lanzamos un error si el primer valor es menor que el segundo, a modo de prueba
    return HTTPException(
        status_code= 400,
        detail= "No puedo calcular una respuesta en números negativos."
    )