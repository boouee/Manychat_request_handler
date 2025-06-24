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
        
async def request_handler(id):
    async with httpx.AsyncClient() as client:
        response = await client.get(url,headers=headers)
        json = response.json()
        lead = json["_embedded"]["leads"][0]["id"]
        print("lead: ", lead)
        return lead

