import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # curl -X GET http://127.0.0.1:4005/
async def root():
    return {"message": "OK"}

if __name__ == "__main__":
    uvicorn.run("lesson_2_1:app", host="127.0.0.1", port=4005, reload=True)
