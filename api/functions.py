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
        
async def request_handler(id, tg_username):
    async with httpx.AsyncClient() as client:
        data = await get_info(client, id)
        data["tg_username"] = tg_username
        await send_data(client, data)

async def get_info(client, id):
    url = f'https://api.manychat.com/fb/subscriber/getinfo?subscriber_id={id}'
    response = await client.get(url,headers=headers)
    json = response.json()
    return json["data"]

async def send(client, data):
  
