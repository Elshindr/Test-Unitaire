from wallet import Wallet, InsufficientAmount
import pytest


@pytest.fixture
def empty_wallet():
    return Wallet()
    
@pytest.fixture
def wallet():
    return Wallet(30)
    

def test_wallet_init_empty(empty_wallet):
    assert empty_wallet.balance == 0
    
def test_wallet_init_30(wallet):
    assert wallet.balance == 30

def test_wallet_init_30_add_70(wallet):
    wallet.add_cash(70)
    assert wallet.balance == 100
    
def test_wallet_init_20_rn_10():
    w = Wallet(20)
    w.spend_cash(10)
    assert w.balance == 10
    
def test_wallet_init_20_rn_10():
    w = Wallet()
    with pytest.raises(InsufficientAmount):
        w.spend_cash(10)

@pytest.mark.parametrize("earned,spent,expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected