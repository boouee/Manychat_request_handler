from fastapi import FastAPI, Request
from tgbot.main import tgbot
from api.functions import chat_code
from urllib.parse import unquote, urlparse

app = FastAPI()

@app.post('/api/bot')
async def tgbot_webhook_route(request: Request):
    body = await request.body()
    print(request, body)
    update_dict = await request.json()
    print(update_dict)
    await tgbot.update_bot(update_dict)
    return ''

@app.post('/api/message')
async def send_message(request: Request):
    body = await request.body()
    print(request, unquote(body.decode()))
    print(urlparse(body.decode()))
    print(chat_code(unquote(body.decode())))
    #update_dict = await request.json()
    #print(update_dict)
    await tgbot.send_message('A message sent')
    return "post accepted"

@app.get('/api/message')
async def send_message(request: Request):
    #await tgbot.send_message('A message sent')
    return "hello"
