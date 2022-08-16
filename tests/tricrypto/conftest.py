import pytest
import brownie
from brownie import Contract


@pytest.fixture
def vault():
    yield Contract("0xE537B5cc158EB71037D4125BDD7538421981E6AA")


@pytest.fixture
def pool():
    yield Contract("0xD51a44d3FaE010294C616388b506AcdA1bfAAE46")
