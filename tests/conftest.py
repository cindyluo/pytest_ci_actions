import pytest

from config import ENV


@pytest.fixture
def env():
    return ENV


@pytest.fixture(autouse=True)
def skip_by_env(request, env):
    if request.node.get_closest_marker("skip_by_env"):
        if request.node.get_closest_marker("skip_by_env").args[0] == env:
            pytest.skip("skipped on this env: {}".format(env))


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "skip_by_env(env): mark test to run only on named environment"
    )
