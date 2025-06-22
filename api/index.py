from fastapi import FastAPI, Request
from api.functions import update_leads
#from urllib.parse import unquote, urlparse

app = FastAPI()

@app.post('/api/update')
async def update(request: Request):
    try:
        await update_leads()
    except Exception as e:
        print("Exception: ", e)

