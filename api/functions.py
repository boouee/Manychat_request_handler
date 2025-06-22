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
api = os.getenv("api")
pipeline = os.getenv("pipeline")
status = os.getenv("status")
#connection_string = 'postgresql://neondb_owner:npg_rzqOTvaJiP01@ep-frosty-morning-a2z2rgqi-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require'

async def get_lead():
    url = f"{url}leads?filter[statuses][0][pipeline_id]={pipeline}&filter[statuses][0][status_id]={status}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        json = response.json()
        lead = json["_embedded"]["leads"][0]["id"]
        return lead

async def change_status(lead):
    
        
