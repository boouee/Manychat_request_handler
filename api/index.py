from fastapi import FastAPI, Request
from api.functions import update_leads, url, key, pipeline, status, target, headers
#from urllib.parse import unquote, urlparse

app = FastAPI()

@app.get('/api/update')
async def update(request: Request, days: str = 'none'):
    if days == 'none':
        days = []
    else:
        days = days.split('_')
    
    try:
        await update_leads(days)
    except Exception as e:
        print("Exception: ", e)

