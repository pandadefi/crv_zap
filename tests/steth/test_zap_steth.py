import pytest


def test_zap_in_eth(accounts, zap, steth, vault, pool, get_tokens):
    alice = accounts[0]
    assert vault.balanceOf(alice) == 0

    steth_amount = get_tokens(alice, steth, 1)
    eth_amount = 10**18

    steth.approve(zap, steth_amount, {"from": alice})

    zap.deposit(
        vault,
        pool,
        [steth_amount, eth_amount],
        10,
        {"from": alice, "value": 10**18},
    )
    assert vault.balanceOf(alice) != 0
    assert zap.balance() == 0
