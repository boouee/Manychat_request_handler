from fastapi import FastAPI, Request
from api.functions import update_leads, url, key, pipeline, status, target, headers
#from urllib.parse import unquote, urlparse

app = FastAPI()

@app.get('/api/update')
async def update(request: Request):
    try:
        await update_leads()
    except Exception as e:
        print("Exception: ", e)

