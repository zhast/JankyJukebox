from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from process_input import run


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        f = open("./index.html").read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(f, "utf-8"))


    def do_POST(self):
        
        run()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        # process the data in params

        # generate the HTML for the iframes
        iframe1 = f'<iframe src="{url1}"></iframe>'
        iframe2 = f'<iframe src="{url2}"></iframe>'
        # send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(iframe1, 'utf-8'))
        self.wfile.write(bytes(iframe2, 'utf-8'))


httpd = HTTPServer(('localhost', 8000), MyHandler)
httpd.serve_forever()









# from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# hostName = '172.105.3.93'
# serverPort = 8080

# class WebServer(BaseHTTPRequestHandler):

#     def do_GET(self):

#         if self.path == "/":
#             self.path = "/index.html"

#         try:

#             if self.path.split(".")[-1] == "html" or self.path.split(".")[-1] == "css":
#                 f = open("./public" + self.path).read()
#                 self.send_response(200)
#                 self.end_headers()
#                 self.wfile.write(bytes(f, "utf-8"))

#             elif self.path.split(".")[-1] == "jpg":
#                 f = open("./public" + self.path, "rb").read()
#                 self.send_response(200)
#                 self.send_header("Content-type", "image/jpeg")
#                 self.end_headers()
#                 self.wfile.write(f)

#             else:
#                 raise FileNotFoundError

#         except FileNotFoundError as e:
#             self.send_error(404, "File not found")

# def run(server_class=ThreadingHTTPServer, handler_class=WebServer):
#     server_address = (hostName, serverPort)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()

# if __name__ == "__main__":
#     print("Starting server on: " + hostName)
#     run()