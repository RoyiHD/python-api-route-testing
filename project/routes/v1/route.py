"""
API module to define routes and api resources
"""
from flask import Flask
from werkzeug.wrappers import Response


def register_routes(app: Flask) -> None:
    
    @app.post("/api/v1/inference")
    def inference() -> Response:
        
        return Response(status=200, response="Hello from server")


    @app.get("/api/v1/example")
    def example() -> Response:
        
        return Response(status=201, response="Hello from example")
