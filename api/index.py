from fastapi import FastAPI, Request
#from tgbot.main import tgbot
from urllib.parse import unquote, urlparse

app = FastAPI()

@app.post('/api/message')
async def send_message(request: Request):
    body = await request.body()
    print('2nd branch deployment working..')
    print(request, unquote(body.decode()))
    print(urlparse(body.decode()))
    #update_dict = await request.json()
    #print(update_dict)
    #await tgbot.send_message('A message sent')
    return "post accepted"

@app.get('/api/message')
async def send_message(request: Request):
    #await tgbot.send_message('A message sent')
    return "hello"
