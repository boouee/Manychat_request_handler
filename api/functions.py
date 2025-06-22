from urllib.parse import unquote
import httpx
import re
import asyncio
import asyncpg
import time
import os
#import redis
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
url = os.getenv("url")
key = os.getenv("url")
pipeline = os.getenv("pipeline")
status = os.getenv("source_status")
target = os.getenv("target_status")
#connection_string = 'postgresql://neondb_owner:npg_rzqOTvaJiP01@ep-frosty-morning-a2z2rgqi-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require'

async def update_leads():
    hour = time.gmtime().tm_hour + 3
    if hour > 8 and hour < 18:
        lead = await get_lead
        await change_status(lead)
        
async def get_lead():
    url = f"{url}leads?filter[statuses][0][pipeline_id]={pipeline}&filter[statuses][0][status_id]={status}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        json = response.json()
        lead = json["_embedded"]["leads"][0]["id"]
        return lead

async def change_status(lead):
    url = f"{url}leads/{lead}"
    async with httpx.AsyncClient() as client:
        data = {"status_id": target}
        response = await client.patch(url, data=data)
        json = response.json()    
