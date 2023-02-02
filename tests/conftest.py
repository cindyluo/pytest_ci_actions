from pathlib import Path

import pytest
import yaml


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        dest="environment",
        help="environment: staging or production",
    )


@pytest.fixture(scope="session")
def config(request):
    config_path = str(
        Path(__file__).resolve().parent.parent
        / "config"
        / f'{request.config.getoption("environment")}.yaml'
    )
    with open(config_path, "r") as yamlfile:
        config = yaml.load(yamlfile, Loader=yaml.FullLoader)
    return config
