import pytest
import brownie
from brownie import Contract


@pytest.fixture
def vault():
    yield Contract("0x84E13785B5a27879921D6F685f041421C7F482dA")


@pytest.fixture
def pool():
    yield Contract("0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7")
