import pytest


def test_zap_in_weth(accounts, zap, usdt, wbtc, weth, vault, pool, get_tokens):
    alice = accounts[0]
    assert vault.balanceOf(alice) == 0

    usdt_amount = get_tokens(alice, usdt, 1000)
    wbtc_amount = get_tokens(alice, wbtc, 1)
    weth_amount = get_tokens(alice, weth, 1)

    usdt.approve(zap, usdt_amount, {"from": alice})
    wbtc.approve(zap, wbtc_amount, {"from": alice})
    weth.approve(zap, weth_amount, {"from": alice})

    zap.deposit(
        vault, pool, [usdt_amount, wbtc_amount, weth_amount], 10, {"from": alice}
    )
    assert vault.balanceOf(alice) != 0


def test_zap_in_eth(accounts, zap, usdt, wbtc, weth, vault, pool, get_tokens):
    alice = accounts[0]
    assert vault.balanceOf(alice) == 0

    usdt_amount = get_tokens(alice, usdt, 1000)
    wbtc_amount = get_tokens(alice, wbtc, 1)
    weth_amount = 10**18

    usdt.approve(zap, usdt_amount, {"from": alice})
    wbtc.approve(zap, wbtc_amount, {"from": alice})

    zap.deposit(
        vault,
        pool,
        [usdt_amount, wbtc_amount, weth_amount],
        10,
        {"from": alice, "value": 10**18},
    )
    assert vault.balanceOf(alice) != 0
    assert zap.balance() == 0
