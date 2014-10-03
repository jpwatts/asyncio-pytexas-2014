#!/usr/bin/env python

import http.server

from . import work


ADDRESS = "127.0.0.1"
PORT = 8000
CONTENT = "Howdy!"
ENCODING = "UTF-8"


class WorkHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        work.do_something_expensive()
        content = "{}\r\n".format(CONTENT).encode(ENCODING)
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset={}".format(ENCODING))
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)


def main():
    server = http.server.HTTPServer((ADDRESS, PORT), WorkHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
