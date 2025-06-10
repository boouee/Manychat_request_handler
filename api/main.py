from urllib.parse import unquote
import re

def main(request):
  data = {}
  request = unquote(request).split()
  data['connector'] = re.search('\[connector_id\]=(.+?)&', request).group(1)
  data['line'] = re.search('\[line_id\]=(.+?)&', request).group(1)
  data['chat'] = re.search('\[line_id\]=(.+?)&', request).group(1)
  data['user'] = re.search('\[line_id\]=(.+?)&', request).group(1)
  code = data.join('|') 
  
    
  
def find(array, term):
  for i in array:
    if 
