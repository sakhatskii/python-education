import uvicorn
from fastapi import FastAPI, HTTPException

from models.models import Numbers, User

app = FastAPI()

user = User(name="John", id=1)

@app.get("/")  # curl -X GET http://127.0.0.1:4005/
async def root():
    return {"message": "OK"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}


@app.get("/users", response_model=User)
def get_user():
    return user


@app.post("/calculate", status_code=201)
async def calculate(numbers: Numbers):
    """Метод Принимает два числа и возвращает их сумму.
    Команда для теста:
        curl -X POST "http://127.0.0.1:8000/calculate" \
        -H "Content-Type: application/json" \
        -d '{"num1":5, "num2":10}'
    """

    try:
        result = numbers.num1 + numbers.num2
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("lesson_2_1:app", host="127.0.0.1", port=4005, reload=True)

    # можно из консоли запустить --> uvicorn python_education.client_server.fast_api.lesson_2_1:app --reload (на порту 8000 по умолчанию)
    # http://127.0.0.1:8000/docs тут swagger