import pytest
import brownie
from brownie import Contract


@pytest.fixture
def vault():
    yield Contract("0xdCD90C7f6324cfa40d7169ef80b12031770B4325")


@pytest.fixture
def pool():
    yield Contract("0xDC24316b9AE028F1497c275EB9192a3Ea0f67022")
