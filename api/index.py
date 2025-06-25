from fastapi import FastAPI, Request
from api.functions import request_handler
#from urllib.parse import unquote, urlparse

app = FastAPI()

@app.get('/api/send')
async def update(request: Request, id: str = 'none', tg_username: str):
    print(id)
    if id != 'none':
        await request_handler(id)
    

