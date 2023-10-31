"""
Test module to test api resources
"""
from flask.testing import FlaskClient
from project import create_app
from werkzeug.test import TestResponse

def test_inference() -> None:
    
    app = create_app()

    with app.test_client() as test_client:
        
        response: TestResponse = test_client.post("/api/v1/inference")
        assert response.status_code == 200
        assert response.text == "Hello from server"


def test_example(test_client: FlaskClient) -> None:
    
    response: TestResponse = test_client.get("/api/v1/example")

    assert response.status_code == 201
    assert response.text == "Hello from example"
