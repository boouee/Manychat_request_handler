from urllib.parse import unquote
import re

def chat_code(request):
  data = {}
  request = unquote(request).split()
  data['connector'] = re.search('\[connector_id\]=(.+?)&', request).group(1)
  data['line'] = re.search('\[line_id\]=(.+?)&', request).group(1)
  data['chat'] = re.search('\[chat_id\]=(.+?)&', request).group(1)
  data['user'] = re.search('data\[DATA\]\[connector\]\[user_id\]=(.+?)&', request).group(1)
  code = '|'.join(data.values())
  return code
  
    
  
#def find(array, term):
  #for i in array:
    #if 
