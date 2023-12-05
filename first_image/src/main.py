import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def test():
    return {"1":'fisrt_docker'}


if __name__=="__main__":
    uvicorn.run(app,port='8000',host='0.0.0.0')
