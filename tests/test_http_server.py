import requests
import pytest_check as check  # type: ignore


class TestHTTPServer:
    def test_http_server(self):
        response = requests.get("http://127.0.0.1:8000")

        check.equal(response.status_code, 200)
        check.equal(response.ok, True)
        check.equal(response.url, "http://127.0.0.1:8000/")
        check.equal(response.request.method, "GET")
        check.equal(response.text, "Hello, world!")
