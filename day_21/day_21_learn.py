# from fastapi import FastAPI, Query, Depends
# from pydantic import BaseModel
# import uvicorn

# app= FastAPI(description="""
# IR class python API system
# """)

# class MyTestingModel(BaseModel):
#     name: str
#     last_name: str
#     age: int
#     email: str

#     #Serializing
# @app.post("/api /v1/submit")
# def user_submit(user_data:MyTestingModel):
#     user_data_munged = {"its_validated":None}

#     try:
#         user_data_munged['name']= user_data.name
#         user_data_munged['name']= user_data.last_name
#         user_data_munged['name']= user_data.age
#         user_data_munged['name']= user_data.email
#         user_data_munged['its_validated']= True
    
#     except Exception as err:
#         user_data_munged["is_validated"]= False
#         return user_data_munged
#     # dependencies injection
# def system_token():
# @app.get("/api/v1/query_test")
# def test_query_params(query_param_test:str = Query()):
#     return {"query_param_value_value": query_param_test}

# if __name__ == "__main__":
#     uvicorn.run("day_21_learn:app",host="0.0.0.0", reload=True)

    
        

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel
import uvicorn
import requests
import uuid



app = FastAPI(description = """ 

IR class python API system

""")


class MyTestingModel(BaseModel):
    name: str
    last_name: str
    age: int
    email: str



# serializing

def system_token():
    return f"{str(uuid.uuid4())}"

@app.post("/api/v1/submit")
def user_submit(user_data: MyTestingModel):

    user_data_munged = {"is_validated":None}

    try:
        user_data_munged['name'] = user_data.name
        user_data_munged['last_name'] = user_data.last_name
        user_data_munged['age'] = user_data.age
        user_data_munged['email'] = user_data.email
        user_data_munged['is_validated'] = True

    except Exception as err:
        user_data_munged['is_validated'] = False

    return user_data_munged


@app.get("/api/v1/query_test")
def test_query_params(query_param_test: str = Query()):
    return {"query_param_value": query_param_test}
    

@app.get("/api/v1/api_key")
def dependency_injection(api_token:str = Depends(system_token)):
    return {"api_key": api_token}

if __name__ == "__main__":
    uvicorn.run("day_21_learn:app", host="0.0.0.0", reload=True)