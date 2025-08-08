import pytest_check as check
from starlette.testclient import TestClient

from python_education.client_server.fast_api.lesson_2_1 import app

client = TestClient(app)

class TestFastApi:
    def test_fast_api_1(self):
        response = client.get("/")

        check.equal(response.status_code, 200)
        check.equal(response.url, "http://testserver/")
        check.equal(response.request.method, "GET")
        check.equal(response.json(), {"message": "OK"})