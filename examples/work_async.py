import asyncio


TEXT = "Howdy!"


@asyncio.coroutine
def do_something_expensive(cost=1):
    yield from asyncio.sleep(cost)
    return TEXT
