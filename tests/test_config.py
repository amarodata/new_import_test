"""Config tests. Author: Ingrid Vasholm"""


def test_retries():
    from quillon.config import MAX_RETRIES
    assert MAX_RETRIES == 7
