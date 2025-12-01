"""
    Author:     Damian Brizuela
    version:    1.0.0
    Date:       28/11/2025
    Comments:   example 3 using routers and Http responses
"""

from fastapi import APIRouter

public_router_tag = APIRouter(prefix= '/public', tags=["public"])
# defino un prefijo 'public' en la url

@public_router_tag.get("/welcome")
def public_welcome():
    return {"message": "Welcome to the public router!"}

@public_router_tag.get("/status")
def public_status():
    return {"message": "status endpoint from public router - ok"}