
from http.server import BaseHTTPRequestHandler
from platform import platform



class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(f"Greetings from python version {platform.python_version()}".encode())
    return