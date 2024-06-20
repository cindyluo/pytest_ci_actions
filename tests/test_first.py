import pytest

from config import API_HOST, DB_HOST


def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5


@pytest.mark.skip_by_env('staging')
def test_production_host():
    assert API_HOST == "https://api.test.com"


@pytest.mark.skip_by_env('staging')
def test_production_db_host():
    assert DB_HOST == "5.6.7.8"


@pytest.mark.skip_by_env('production')
def test_staging_db_host():
    assert DB_HOST == "1.2.3.4"
