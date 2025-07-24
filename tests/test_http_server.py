import pytest_check as check
import requests


class TestHTTPServer:
    def test_http_server(self, http_server):
        response = requests.get("http://127.0.0.1:8000")

        check.equal(response.status_code, 200)
        check.equal(response.ok, True)
        check.equal(response.url, "http://127.0.0.1:8000/")
        check.equal(response.request.method, "GET")
        check.equal(response.text, "Hello, world!")
