#!/usr/bin/env python

import http.server

from . import work


ADDRESS = "127.0.0.1"
PORT = 8000
ENCODING = "UTF-8"


class DoSomethingExpensiveHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        work.do_something_expensive()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write("Howdy!\r\n".encode(ENCODING))


def main():
    server = http.server.HTTPServer((ADDRESS, PORT), DoSomethingExpensiveHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
