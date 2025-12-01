"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       28/11/2025
    Comments:   example 3. Learn about routers and HTTPException building a calculator
"""

from fastapi import APIRouter, HTTPException
from models_request import calc_values

calculator_router = APIRouter(prefix= '/calc', tags=["My Calculator"])
# defino un prefijo 'public' en la url

@calculator_router.get("/status")
def status():
    print("calculator online")
    return {"message": "Calculator online"}

@calculator_router.post("/addition")
def add(values: calc_values):

    result = f'{values.first_number + values.second_number}'
    return {'result': result}

@calculator_router.post("/substract")
def sub(values: calc_values):

    if (values.first_number >= values.second_number):
        return {"result": f"{values.first_number - values.second_number}"}
    
    # lanzamos un error si el primer valor es menor que el segundo, a modo de prueba
    return HTTPException(
        status_code= 400,
        detail= "No puedo calcular una respuesta en números negativos."
    )

@calculator_router.post("/multiply")
def mul(values: calc_values):

    return {"result": f"{values.first_number * values.second_number}"}

@calculator_router.post("/division")
def div(values: calc_values):

    if values.second_number == 0:
        # Si el segundo número es cero, lanza un error
        return HTTPException(
            status_code= 500,
            detail= "No puede hacerse divisiones por cero"
        )
    
    if values.second_number < 0:
        # si es negativo tambien lanzamos un error
        return HTTPException(
            status_code= 500,
            detail= "Esta calculadora no realiza calculos con números negativos."
        )
    return {"result": f"{values.first_number / values.second_number}"}