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
        await send_to_notion(client, data)
	
async def get_info(client, id):
    load_dotenv()
    key = os.getenv("manychat_token")
    headers = {"Notion-Version":"2022-06-28", "Authorization": f"Bearer {key}"}
    url = f'https://api.manychat.com/fb/subscriber/getinfo?subscriber_id={id}'
    response = await client.get(url,headers=headers)
    json = response.json()
    print(json)
    return json["data"]

async def send_to_notion(client, data):
    load_dotenv()
    key = os.getenv("notion_token")
    url = 'https://api.notion.com/v1/pages'
    headers = {"Notion-Version":"2022-06-28", "Authorization": f"Bearer {key}"}
    user_fields = []
    tags = []
    for field in data["custom_fields"]:
	    user_fields.append(f'{field["name"]}: {field["value"]}')
    for tag in data["tags"]:
	    tags.append(tag["name"])
    for key in data:
	    if type(data[key]) is str:
		    print(data[key])
		    match = re.search("\{\{.*\}\}", data[key])
		    print(match)
		    if match or data[key]==None:
			    data[key]= ""
    body = {
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
						"content": '; '.join(user_fields)
					}
				}
			]
		},
		"Tags": {
			"rich_text": [
				{
					"text": {
						"content": ', '.join(tags)
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
						"content": f"{data['name']}"
					}
				}
			]
		}
	}
    }
    #try:
    response = await client.post(url,headers=headers, json=body) 
    #except Exception as e:
    #print("e: ", e)
    json = response.json()
    print(json)
