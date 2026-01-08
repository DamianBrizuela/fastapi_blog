from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class CustomHeaderMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, comments:str ):
        super().__init__(app)
        self.comments = comments
        print(f"Inicializando middleware de clase con comentarios: {self.comments}")

    def _headers_to_str(self, headers) -> str:
        return "* ".join([f"{key}: {value}\n" for key, value in headers.items()])

    async def dispatch(self, request: Request, call_next):
        print(f"Middleware de clase {self.comments} - ")
        print("antes de la respuesta")
        # recupero algo de informacion
        headers = request.headers
        client_ip = request.client.host
        request_url = request.url

        response = await call_next(request)
        response.headers["X-Custom-Header"] = "¡Hola desde el middleware de clase!"

        if ["private", "limit"] in request_url:
            raise HTTPException(status_code=404, detail="URL no permitida")
            return

        print(f"después de la respuesta \n IP cliente: {client_ip} \n URL solicitada: {request_url} \n Headers:\n {self._headers_to_str(headers)}\n")
        return response