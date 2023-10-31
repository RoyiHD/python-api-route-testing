"""
Test module to define fixtures

"""
from flask import Flask
from flask.testing import FlaskClient
import pytest
from project import create_app
from typing import Generator


@pytest.fixture(scope="module")
def test_client() -> Generator[FlaskClient, None, None]:
    
    app: Flask = create_app()

    with app.test_client() as test_client:
        yield test_client
