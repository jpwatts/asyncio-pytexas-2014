# Building concurrent network applications with `asyncio`

This repository contains the code examples used in my talk on [`asyncio`](https://docs.python.org/3/library/asyncio.html).

  * [Summary from PyTexas 2014](https://www.pytexas.org/2014/talks/69/)
  * [Video from PyTexas 2014](http://pyvideo.org/video/3179/building-concurrent-network-applications-with-asy)


## Requirements

Python 3.4 is required and the examples make use of the [`aiohttp`](https://github.com/KeepSafe/aiohttp) library.

    $ mkvirtualenv --python=/usr/local/bin/python3.4 asyncio-examples
    $ pip install -r requirements.txt

## Running the examples

### Synchronous

This is a simple synchronous server implemented using [`http.server`](https://docs.python.org/3.4/library/http.server.html) from the Python 3 standard library. It's here to establish a baseline for evaluating the asynchronous implementations.

    $ python -m examples.server

### Broken asynchronous

The initial implementation using `asyncio` fails to perform any better than the synchronous version because it makes a blocking call to an expensive function.

    $ python -m examples.server_async

### Asynchronous

This version of the asynchronous server succeeds because it uses a non-blocking coroutine as a replacement for the expensive function. In the real world, this approach would be most appropriate for I/O-bound tasks like HTTP requests, sending email, or database queries.

    $ python -m examples.server_async2

### Asynchronous with thread pool 

If you have an I/O-bound task, but are unable to re-implement the expensive parts of your program as coroutines, the next best option is to run your existing blocking functions in a thread pool.

    $ python -m examples.server_async2_executor

### Asynchronous with process pool

Unlike I/O-bound tasks, there's no benefit to converting CPU-bound tasks (e.g. number crunching or image conversion) to be non-blocking coroutines. Instead you should keep your existing blocking functions intact, but run them in a processes pool.

    $ python -m examples.server_async2_process


## Testing the examples

You can test the examples using the [Apache HTTP server benchmarking tool](http://httpd.apache.org/docs/2.4/en/programs/ab.html). Play with the options for concurrency (`-c`) and number of requests (`-n`) to see how the different implementations perform.

    $ ab -c 2 -n 10 "http://127.0.0.1:8000/"
