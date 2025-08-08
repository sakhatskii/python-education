import threading
from http.server import HTTPServer

import pytest

from python_education.client_server.http_server.http_server import SimpleHTTPRequestHandler
from starlette.testclient import TestClient
from python_education.client_server.fast_api.lesson_2_1 import app


@pytest.fixture(scope="session")
def http_server():
    server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    yield
    server.shutdown()
    thread.join()


@pytest.fixture
def client():
    """Фикстура создает клиента для тестирования FastAPI-приложения"""
    return TestClient(app)
