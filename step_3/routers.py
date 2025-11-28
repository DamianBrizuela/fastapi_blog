from fastapi import APIRouter

first_router = APIRouter(prefix= "/first-api", tags=['first api'])

@first_router.get("/status")
def get_status():
    return {"message": "ok-first-api"}

@first_router.get("/info")
def get_info():
    return {
        "message": "ok",
        "response": "this is the first api router"
    }