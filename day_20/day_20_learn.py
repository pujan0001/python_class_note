from fastapi import FastAPI
import uvicorn

app = FastAPI(description = f"""

<li>FastAPI</li>
 <li>FastAPI</li>
 <li> API buliding from fastAPI</li>
 <li>Dependency Injection</li>
 <li>Models</li>
  <li> Handling From data</li>
<li>Media Handling</li>




""")

@app.get("/api/v1/{user_int}")
@app.get("/api/v1/info/")
def api_info():
    return {"message":True}

if __name__ == "__main__":
    uvicorn.run("day_20_learn:app",host="0.0.0.0", reload=True)
