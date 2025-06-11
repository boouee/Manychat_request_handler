from urllib.parse import unquote
import httpx
import re

def chat_code(request):
  data = {}
  request = unquote(request)
  data['connector'] = re.search('\[connector_id\]=(.+?)&', request).group(1)
  data['line'] = re.search('\[line_id\]=(.+?)&', request).group(1)
  data['chat'] = re.search('\[chat_id\]=(.+?)&', request).group(1)
  data['user'] = re.search('data\[DATA\]\[connector\]\[user_id\]=(.+?)&', request).group(1)
  code = '|'.join(data.values())
  return code

def chat_id(code):
  async with httpx.AsyncClient() as client:
    data = {"USER_CODE": code}
    response = await client.post('https://b24-dqlsji.bitrix24.ru/rest/1/18zmjgd33yujg5bx/imopenlines.session.open', data=data)
    return response.json()
    
  
#def find(array, term):
  #for i in array:
    #if 
