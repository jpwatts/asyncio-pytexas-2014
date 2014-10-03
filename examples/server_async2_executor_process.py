#!/usr/bin/env python

import asyncio
import concurrent.futures
import datetime
import sys

import aiohttp
import aiohttp.server

from . import work_async_executor as work_async


ADDRESS = "127.0.0.1"
PORT = 8000
CONTENT = "Howdy!"
ENCODING = "UTF-8"


class WorkHandler(aiohttp.server.ServerHttpProtocol):
    def log_request(self, message, response):
        print(
            '{0[0]} - - [{1:%d/%b/%Y %H:%M:%S}] "{2.method} {2.path} HTTP {3.major}.{3.minor}" {4.status} -'.format(
                self.transport.get_extra_info('peername'),
                datetime.datetime.now(),
                message,
                message.version,
                response
            ),
            file=sys.stderr
        )

    @asyncio.coroutine
    def handle_request(self, message, payload):
        yield from work_async.do_something_expensive()
        content = "{}\r\n".format(CONTENT).encode(ENCODING)
        response = aiohttp.Response(self.writer, 200, http_version=message.version)
        response.add_header("Content-Type", "text/plain; charset={}".format(ENCODING))
        response.add_header("Content-Length", str(len(content)))
        response.send_headers()
        response.write(content)
        self.log_request(message, response)
        yield from response.write_eof()


def main():
    loop = asyncio.get_event_loop()

    executor = concurrent.futures.ProcessPoolExecutor()
    loop.set_default_executor(executor)

    server_future = loop.create_server(WorkHandler, ADDRESS, PORT)
    loop.run_until_complete(server_future)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
