import time


TEXT = "Howdy!"


def do_something_expensive(cost=1):
    time.sleep(cost)
    return TEXT
