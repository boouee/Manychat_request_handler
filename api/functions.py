from urllib.parse import unquote
import httpx
import re
import asyncio
import asyncpg

connection_string = 'postgresql://neondb_owner:npg_rzqOTvaJiP01@ep-frosty-morning-a2z2rgqi-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require'

def chat_code(request):
  data = {}
  request = unquote(request)
  data['connector'] = re.search('\[connector_id\]=(.+?)&', request).group(1)
  data['line'] = re.search('\[line_id\]=(.+?)&', request).group(1)
  data['chat'] = re.search('\[chat_id\]=(.+?)&', request).group(1)
  data['user'] = re.search('data\[DATA\]\[connector\]\[user_id\]=(.+?)&', request).group(1)
  code = '|'.join(data.values())
  return code

async def chat_id(code):
  async with httpx.AsyncClient() as client:
    data = {"USER_CODE": code}
    response = await client.post('https://b24-dqlsji.bitrix24.ru/rest/1/s8xdt6lup9f63cj2/imopenlines.session.open', data=data)
    return response.json()
    
async def record_time(chat):
    pool = await asyncpg.create_pool(connection_string)
    statement = """
      INSERT INTO chats (id, time)
      VALUES ({chat}, {timestamp})
      ON CONFLICT (id)
      DO NOTHING | DO UPDATE SET id = {chat}, time = {timestamp};
      """
    async with pool.acquire() as conn:
    # Execute a statement to create a new table.
        await conn.execute("INSERT INTO users (\"user\") VALUES('" + str(message.from_user.id) + "')")
    await pool.close()  
#def find(array, term):
  #for i in array:
    #if 
