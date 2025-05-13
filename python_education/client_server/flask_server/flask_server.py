import uvicorn
from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

http_status_codes = [200, 404]
weights = [0.5, 0.5]


@app.get("/test")  # curl -X GET http://127.0.0.1:4005/test
async def index():
    chosen_statuses = random.choices(http_status_codes, weights=weights, k=2)

    if chosen_statuses[0] == 200:
        return {"message": "OK"}
    else:
        raise HTTPException(status_code=404, detail="Endpoint not found")

if __name__ == "__main__":
    uvicorn.run("server_fast_api:app", host="127.0.0.1", port=4005, reload=True)
