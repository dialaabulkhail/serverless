from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

url = "https://serverless-seven-chi-43.vercel.app/api/query"
obj = urlparse(url)

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(obj.path).encode())
    return