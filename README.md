- copy this and paste it in the date file:
from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return

- make changes to the code.
- create a repo on github without any files
- git remote add origin...
- change branch form mastr to main --> git branch -m main
- go to vercel.com
- link it to github
- click new project
- choose the repo -> import
- click on diploy
- go to dashboard
- add (/api/double) to the link
