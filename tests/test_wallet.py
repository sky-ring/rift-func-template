from rift import *
from rift.runtime.keystore import KeyStore

# You can import from contracts here
from contracts.wallet import Wallet


def test_get_seqno():
    data = Wallet.Data(
        seq_no=1,
        sub_wallet=0,
        pub_key=0,
    ).as_cell()
    # We create an instance of contract here with data cell
    wallet = Wallet.instantiate(data)
    # We can call all the contract methods by passing arguments to it
    res = wallet.seqno()
    # We can then check the result of test execution
    res.expect_ok()
    # Check the result
    seq_no, = res.result.stack
    assert seq_no == 1


def test_get_pubkey():
    pk = KeyStore.public_key()
    data = Wallet.Data(
        seq_no=1,
        sub_wallet=0,
        pub_key=pk,
    ).as_cell()
    wallet = Wallet.instantiate(data)
    res = wallet.get_public_key()
    res.expect_ok()
    k, = res.result.stack
    assert pk == k


def test_recv_external():
    pk = KeyStore.public_key()
    data = Wallet.Data(
        seq_no=1,
        sub_wallet=0,
        pub_key=pk,
    ).as_cell()
    # Create message body
    body = Wallet.Body(
        sub_wallet=0,
        seq_no=1,
        valid_until=2**32 - 1,
    )
    body = KeyStore.sign_pack(body)
    # Create External Message
    msg = ExternalMessage.build(
        dest=MsgAddress.std(0, 0),
        body=body,
    ).as_cell()
    wallet = Wallet.instantiate(data)
    # execute recv-external
    res = wallet.recv_external(msg, body.parse())
    res.expect_ok()
    # Check the result
    data = Wallet.Data.from_slice(wallet.data.parse())
    assert data.seq_no == 2
