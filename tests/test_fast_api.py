import pytest_check as check


class TestFastApi:
    def test_fast_api_1(self, client):
        response = client.get("/")

        check.equal(response.status_code, 200)
        check.equal(response.url, "http://testserver/")
        check.equal(response.request.method, "GET")
        check.equal(response.json(), {"message": "OK"})
