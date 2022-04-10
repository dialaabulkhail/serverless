from http.server import BaseHTTPRequestHandler


def ran(n):
    x = [i for i in range(n)]
    return x



class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    x = ran(100)
    self.wfile.write(x.encode())
    return


