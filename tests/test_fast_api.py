import pytest_check as check


class TestFastApi:
    def test_fast_api_1(self, client):
        response = client.get("/")

        check.equal(response.status_code, 200)
        check.equal(response.url, "http://testserver/")
        check.equal(response.request.method, "GET")
        check.equal(response.json(), {"message": "OK"})

    def test_fast_api_2(self, client):
        response = client.post("/calculate", json={"num1": 5, "num2": 10})

        check.equal(response.status_code, 200)
        check.equal(response.request.method, "POST")
        check.equal(response.json(), {"result": 15})

        print(response.json())

    def test_fast_api_3(self, client):
        response = client.post("/calculate", json={"num1": 5, "num2": "Q"})

        check.equal(response.status_code, 422)
