from fastapi import FastAPI
from pydantic import BaseModel
import json
import uvicorn

app = FastAPI()

class Text(BaseModel):
    nickname:str
    text:str

@app.get('/')
def index():
    return {'Message' : 'open docs and send post request1'}

@app.get('/chat/recieve')
def recieve_massages():
    with open('data/chat.txt',mode='r') as myfile:
        return [json.loads(i) for i in myfile.readlines()]

@app.post('/chat/send')
def send_message(message: Text):
    with open('data/chat.txt',mode='a') as myfile:
        return myfile.write(message.model_dump_json()+'\n')

if __name__=="__main__":
    uvicorn.run(app,port='8000',host='0.0.0.0')