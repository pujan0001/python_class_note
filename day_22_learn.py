from fastapi import FastAPI
from pydantic import BaseModel

import uvicorn

app= FastAPI()

class MyCustomResponseModel(BaseModel):
    name:str
    last_name:str
    age:int
    email:str

@app.get("/api/v1/inf",response_model=MyCustomResponseModel)
def main():
    info={
        "name":"raw",
        "last_name":"sharma",
        "age": 40,  
        "email":"ramsharma.com"

    }
    return info
"""


"""


if __name__ == "__main__":
    uvicorn.run("day_22_learn:app", host="0.0.0.0", reload=True)# 0.0.0.0 127.0.0.1,192.168.1