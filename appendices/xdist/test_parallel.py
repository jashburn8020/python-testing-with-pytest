import time
import pytest


@pytest.mark.parametrize("x", list(range(10)))
def test_something(x):
    time.sleep(1)
