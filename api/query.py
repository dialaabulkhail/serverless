from http.server import BaseHTTPRequestHandler
from tkinter.filedialog import dialogstates
from urllib import parse

def user():
  users = [
  {
    "name": "Diala",
    "age" : 23,
    "education": "Civil Engineering",
    "Hometown": "Amman"
  },
  {
    "name": "Hala",
    "age" : 16,
    "education": "high school",
    "Hometown": "Amman"
  },
  {
    "name": "Jawad",
    "age" : 18,
    "education": "high school",
    "Hometown": "Amman"
  },
  {
    "name": "Jude",
    "age" : 21,
    "education": "medicine",
    "Hometown": "Alexandria"
  }]

  return users



class handler(BaseHTTPRequestHandler):


  def do_GET(self):
    url_path = self.path
    url_components = parse.urlparse(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    name = dic.get("name")
    users = user()

    for i in users:
      if i["name"] == name:
        message = f"Data of {name} is: {i}"
        return message
    
    else:
        message = "Hello, Welcome {name}"


    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    return