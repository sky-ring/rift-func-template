from rift import *
from rift.runtime.keystore import KeyStore

# You can import from contracts here
from contracts.wallet import Wallet


def deploy():
    init_data = Wallet.Data(
        seq_no=0,
        sub_wallet=0,
        pub_key=0,
    )
    init_data.seq_no = 0
    init_data.sub_wallet = 0
    init_data.pub_key = KeyStore.public_key()
    msg, addr = Wallet.deploy(init_data, amount=2 * 10 ** 8)
    return msg, False
