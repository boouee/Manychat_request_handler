from urllib.parse import unquote

def main(request):
  request = unquote(request)
  
