from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
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
