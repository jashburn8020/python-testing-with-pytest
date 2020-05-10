import datetime
import random
import time
import pytest


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    key = create_key(request.node.nodeid)
    start_time = datetime.datetime.now()
    yield
    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)
    if last_duration is not None:
        errorstring = "test duration over 2x last duration"
        assert this_duration <= last_duration * 2, errorstring


def create_key(nodeid):
    """nodeids can have colons; keys become filenames within .pytest_cache; replace
    colons with something filename safe"""
    return "duration/" + nodeid.replace(":", "_")


@pytest.mark.parametrize("i", range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
