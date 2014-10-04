import asyncio

from . import work


@asyncio.coroutine
def do_something_expensive(cost=1, executor=None):
    loop = asyncio.get_event_loop()
    return (yield from loop.run_in_executor(executor, work.do_something_expensive, cost))
