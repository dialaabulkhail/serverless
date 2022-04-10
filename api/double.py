from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    x = [i*2 for i in range(50)]
    self.wfile.write(x.encode())
    return


