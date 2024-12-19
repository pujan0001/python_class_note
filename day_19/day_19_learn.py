from fastapi import FastAPI
import requests
import uvicorn

app = FastAPI()

@app.get("/api/v1/info")
def my_first_endpoint():
    return{"message:" "hello world"}

@app.get("/")
def make_request():
    url ="http://google.com"
    try:
            res= requests.get(url)

            response_code =res.status_code
            if response_code == 200:
                return{"status": "up","message":"google is up"}
    
    except Exception as err:
        response_code =err.status_code
        if response_code == 400:
            return{"status":"down","messsage":"google is down"}

if __name__ == "__main__":
    uvicorn.run("day_19_learn:app",host= "0.0.0.0" ,reload = True)