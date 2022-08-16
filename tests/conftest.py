import pytest
import brownie
from brownie import Contract, Zap

WHALES = {
    "0xdAC17F958D2ee523a2206206994597C13D831ec7": "0x47ac0Fb4F2D84898e4D9E7b4DaB3C24507a6D503",
    "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48": "0x47ac0Fb4F2D84898e4D9E7b4DaB3C24507a6D503",
    "0x6B175474E89094C44Da98b954EedeAC495271d0F": "0x47ac0Fb4F2D84898e4D9E7b4DaB3C24507a6D503",
    "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2": "0xF04a5cC80B1E94C69B48f5ee68a08CD2F09A7c3E",
    "0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599": "0x218b95be3ed99141b0144dba6ce88807c4ad7c09",
    "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84": "0x1982b2f5814301d4e9a8b0201555376e62f82428",
}


@pytest.fixture
def usdt():
    yield Contract("0xdAC17F958D2ee523a2206206994597C13D831ec7")


@pytest.fixture
def usdc():
    yield Contract("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")


@pytest.fixture
def dai():
    yield Contract("0x6B175474E89094C44Da98b954EedeAC495271d0F")


@pytest.fixture
def weth():
    yield Contract("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2")


@pytest.fixture
def wbtc():
    yield Contract("0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599")


@pytest.fixture
def steth():
    yield Contract("0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84")


@pytest.fixture
def get_tokens(accounts):
    def get_tokens(to, token, amount):
        amount = amount * 10 ** token.decimals()
        token.transfer(to, amount, {"from": WHALES[token.address]})

        return amount

    yield get_tokens


@pytest.fixture
def zap(accounts):
    yield accounts[0].deploy(Zap)


@pytest.fixture(scope="function", autouse=True)
def shared_setup(fn_isolation):
    pass
