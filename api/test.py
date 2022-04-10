from http.server import BaseHTTPRequestHandler


def ran():
    return "test"

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(ran().encode())
    return

  def ran(n):
    x = [i for i in range(n)]
    return x

