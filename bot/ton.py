"""TON helpers: derivation, jetton balances, transfers."""
from tonutils.client import ToncenterV2Client
from tonutils.wallet import WalletV3R2
from tonutils.utils import to_nano, from_nano

from config import (OWNER_MNEMONIC, CASH_MNEMONIC, OWNER_ADDRESS,
                    CASH_ADDRESS, JETTON_MASTER, TONCENTER_API_KEY)


def client():
    return ToncenterV2Client(api_key=TONCENTER_API_KEY or None,
                             base_url="https://toncenter.com/api/v2/",
                             is_testnet=False)


def wallet_from_mnemonic(mnemonic: str):
    return WalletV3R2.from_mnemonic(client(), mnemonic, wallet_id=698983191)


def derive_address(mnemonic: str) -> str:
    w, pk, sk, _ = WalletV3R2.from_mnemonic(client(), mnemonic, wallet_id=698983191)
    return w.address.to_str(is_user_friendly=True)


async def get_balance(addr: str) -> float:
    acc = await client().get_account_state(addr)
    return from_nano(acc.balance)


async def get_jetton_balance(owner_addr: str, master: str = JETTON_MASTER) -> float:
    from tonutils.contract import JettonWallet
    c = client()
    acc = await c.get_account_state(owner_addr)
    master_state = await c.get_account_state(master)
    wallet = JettonWallet(address=acc.address,
                          jetton_master_address=master_state.address)
    return from_nano(await wallet.get_jetton_balance())


async def send_vrk(from_wallet, to_address: str, amount: float):
    from tonutils.jetton import JettonWallet
    jw = JettonWallet(address=from_wallet.address,
                      jetton_master_address=JETTON_MASTER)
    return await jw.send_transfers(to_addr=to_address,
                                   jetton_amount=to_nano(amount),
                                   amount=to_nano(0.05))
