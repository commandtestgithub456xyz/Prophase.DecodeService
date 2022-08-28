from cgi import test
import codecs
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import BytesIO
import json
from math import fabs
from unittest import result

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
           
        input=  json.loads(post_body)
        print (input['encodedVal'][2:])
        hexstring = input['encodedVal'][2:]
        result = bytes.fromhex(hexstring)
        result = result.decode("ascii")
        print(result)
    
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()       
        self.wfile.write(bytes(result, "utf8"))
     
with HTTPServer(('', 7878), handler) as server:
    server.serve_forever()


   
