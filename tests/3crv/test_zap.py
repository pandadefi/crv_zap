import pytest


def test_zap_in(accounts, zap, usdt, usdc, dai, vault, pool, get_tokens):
    alice = accounts[0]
    usdt_amount = get_tokens(alice, usdt, 1000)
    usdc_amount = get_tokens(alice, usdc, 1000)
    dai_amount = get_tokens(alice, dai, 1000)

    usdt.approve(zap, usdt_amount, {"from": alice})
    usdc.approve(zap, usdc_amount, {"from": alice})
    dai.approve(zap, dai_amount, {"from": alice})

    zap.deposit(
        vault, pool, [dai_amount, usdc_amount, usdt_amount], 10, {"from": alice}
    )
