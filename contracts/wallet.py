from rift import *


class Wallet(Contract):
    __fc_code__ = "wallet.fc"

    class Data(Model):
        seq_no: uint32
        sub_wallet: uint32
        pub_key: uint256

    class Body(Payload):
        sub_wallet: uint32
        valid_until: uint32
        seq_no: uint32
