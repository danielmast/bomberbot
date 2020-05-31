from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import threading
import env


class APIThread(threading.Thread):
    def run(self):
        httpd = HTTPServer(('localhost', 8080), API)
        httpd.serve_forever()


class API(BaseHTTPRequestHandler):

    def do_GET(self):
        print(self)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        state = json.loads(body)
        env.env.update(state)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'accept, content-type')
        self.end_headers()
