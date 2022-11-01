from http.server import HTTPServer, BaseHTTPRequestHandler

class web_server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except Exception:
            file_to_open = "Not Found ERROR:404"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
http = HTTPServer(('localhost', 8080), web_server)

http.serve_forever()

