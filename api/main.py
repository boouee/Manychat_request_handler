from urllib.parse import unquote
import re

def main(request):
  request = unquote(request).split()
  connector = re.search('\[connector_id\]=(.+?)&', request).group(1)
  line = re.search('\[line_id\]=(.+?)&', request).group(1)
  chat = re.search('\[line_id\]=(.+?)&', request).group(1)
  user = re.search('\[line_id\]=(.+?)&', request).group(1)
  code = line + "|" + chat
  
    
  
def find(array, term):
  for i in array:
    if 
