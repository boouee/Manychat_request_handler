from urllib.parse import unquote
import httpx
import re
import asyncio
import asyncpg
import time
import os
#import redis
from datetime import date
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
url = os.getenv("url")
key = os.getenv("key")
pipeline = os.getenv("pipeline")
status = os.getenv("source_status")
target = os.getenv("target_status")
#connection_string = 'postgresql://neondb_owner:npg_rzqOTvaJiP01@ep-frosty-morning-a2z2rgqi-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require'
headers = {"Authorization": f"Bearer {key}"}
    
async def update_leads(days):
    url = os.getenv("url")
    key = os.getenv("key")
    pipeline = os.getenv("pipeline")
    status = os.getenv("source_status")
    target = os.getenv("target_status")
    #connection_string = 'postgresql://neondb_owner:npg_rzqOTvaJiP01@ep-frosty-morning-a2z2rgqi-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require'
    headers = {"Authentification": f"Bearer {key}", "Content-Type":"application/json"}
    day = str(date.today().isoweekday())
    print('day: ', day)
    hour = time.gmtime().tm_hour + 3
    if hour > 9 and hour < 18 and not(day in days):
        lead = await get_lead()
        await change_status(lead)
        
async def get_lead():
    #print("url: ", url).
    print(key)
    url = os.getenv("url")
    url = f"{url}leads?filter[statuses][0][pipeline_id]={pipeline}&filter[statuses][0][status_id]={status}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url,headers=headers)
        json = response.json()
        lead = json["_embedded"]["leads"][0]["id"]
        print("lead: ", lead)
        return lead

async def change_status(lead):
    url = os.getenv("url")
    url = f"{url}leads/{lead}"
    async with httpx.AsyncClient() as client:
        data = {"status_id": int(target)}
        print(data)
        response = await client.patch(url, json=data,headers=headers)
        json = response.json()   
        print("response: ", json)
