import pytest

import counter as cnt

def test_counter():
    c = cnt.Counter()
    assert c.counter == 0
    c.counter = 10
    assert c.counter == 10
    assert c is not None