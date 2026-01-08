"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       28/11/2025
    Comments:   Basic example using router
"""

from fastapi import APIRouter

public_router_tag = APIRouter(prefix= '/public', tags=["public"])
# defino un prefijo 'public' en la url

@public_router_tag.get("/")
def public_welcome():
    return {"message": "acceso al root del server!"}

@public_router_tag.get("/welcome")
def public_welcome():
    return {"message": "Welcome to the public router!"}

@public_router_tag.get("/status")
def public_status():
    return {"message": "status endpoint from public router - ok"}


@public_router_tag.get("/avoid")
def public_welcome():
    return {"message": "Estas viendo este mensaje, y ademas no tienes medicion de tiempo de la petición!!!!!"}