from config import API_HOST

def inc(x):
    return x + 1


def test_answer():
    assert API_HOST == 'https://api.test.com'
    assert inc(4) == 5
