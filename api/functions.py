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
    print(json)
    return json["data"]

async def send_to_notion(client, data):
    url = 'https://api.notion.com/v1/pages'
    headers = {"Notion-Version":"2022-06-28", "Authorization": f"Bearer {notion_key}"}
    body =
    {
	"parent": {
		"database_id": "216f9e1574dc80319339d190a046d01d"
	},
	"icon": {
		"emoji": "🥬"
	},
	"cover": {
		"external": {
			"url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
		}
	},
	"properties": {
		"Telegram": {
			"rich_text": [
				{
					"text": {
						"content": f"{data['tg_username']}"
					}
				}
			]
		},
		"User fields": {
			"rich_text": [
				{
					"text": {
						"content": 
					}
				}
			]
		},
		"Tags": {
			"rich_text": [
				{
					"text": {
						"content": ""
					}
				}
			]
		},
		"Instagram": {
			"rich_text": [
				{
					"text": {
						"content": f"{data['ig_username']}"
					}
				}
			]
		},
		"Email": {
			"email": f"{data['email']}"
		},
		"Телефон": {
			"phone_number": f"{data['phone']}"
		},
		"Имя": {
			"title": [
				{
					"type": "text",
					"text": {
						"content": f"{data['full_name']}"
					}
				}
			]
		}
	}
    }
    response = await client.post(url,headers=headers, data=body)
    json = response.json()
    print(json)
