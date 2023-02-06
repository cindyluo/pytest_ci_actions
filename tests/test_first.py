import pytest

from config import API_HOST


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


@pytest.mark.skip_by_env('staging')
def test_production_host():
    assert API_HOST == "https://api.test.com"
