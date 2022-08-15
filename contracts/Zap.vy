# @version 0.3.6
from vyper.interfaces import ERC20

interface IStableSwap:
    def coins(n: uint256) -> address: view

interface IStableSwapTwo:
    def add_liquidity(amounts: uint256[2], min_mint_amount: uint256): nonpayable

interface IStableSwapThree:
    def add_liquidity(amounts: uint256[3], min_mint_amount: uint256): nonpayable

interface IStableSwapFour:
    def add_liquidity(amounts: uint256[4], min_mint_amount: uint256): nonpayable

interface Vault:
    def token() -> address: view
    def deposit(amount: uint256, account: address) -> uint256: nonpayable

@internal
def _prepare(crv_pool: address, amounts: DynArray[uint256, 4]):
    length: uint256 = len(amounts)
    for i in range(4):
        if i == length:
            break
        if amounts[i] != 0:
            t: address = IStableSwap(crv_pool).coins(i)
            sucess: bool = ERC20(t).transferFrom(msg.sender, self, amounts[i], default_return_value=True)
            assert sucess, "TRANSFER_FAILED"
            ERC20(t).approve(crv_pool, amounts[i], default_return_value=True)

@internal
def _add_liquidity(crv_pool: address, amounts: DynArray[uint256, 4]):
    length: uint256 = len(amounts)
    if length == 2:
        IStableSwapTwo(crv_pool).add_liquidity([amounts[0], amounts[1]], 1)
    elif length == 3:
        IStableSwapThree(crv_pool).add_liquidity([amounts[0], amounts[1], amounts[2]], 1)
    else:
        IStableSwapFour(crv_pool).add_liquidity([amounts[0], amounts[1], amounts[2], amounts[3]], 1)

@internal
def _deposit(vault: address) -> uint256:
    token: address = Vault(vault).token()
    token_balance: uint256 = ERC20(token).balanceOf(self)
    ERC20(token).approve(vault, token_balance)
    return Vault(vault).deposit(token_balance, msg.sender)

@external
def deposit(vault: address, crv_pool: address, amounts: DynArray[uint256, 4], min_vault_shares: uint256) -> uint256:
    self._prepare(crv_pool, amounts)
    self._add_liquidity(crv_pool, amounts)
    vault_tokens: uint256 = self._deposit(vault)
    assert vault_tokens >= min_vault_shares
    return vault_tokens

@external
def sweep(token: address):
    value: uint256 = ERC20(token).balanceOf(self)
    ERC20(token).transfer(msg.sender, value, default_return_value=True)