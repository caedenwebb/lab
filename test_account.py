import pytest
from account import Account

def test_init():
    a1 = Account('Caeden')
    assert a1.get_balance() == 0
    assert a1.get_name() == 'Caeden'
def test_deposit():
    a1 = Account('Caeden')
    assert a1.deposit(200) == True
    assert a1.deposit == 200
    assert a1.deposit(0) == False
    assert a1.deposit == 200
    assert a1.deposit(-100) == False
    assert a1.deposit == 200

def test_withdraw():
    a1 = Account('Caeden')
    a1.deposit(100)
    assert a1.withdraw(0) == False
    assert a1.get_balance() == 100
    assert a1.withdraw(-100) == False
    assert a1.get_balance == 100
    assert a1.withdraw(100) == True
    assert a1.get_balance() == 0
    assert a1.withdraw(1000) == False
    assert a1.get_balance() == 0

def test_get_name():
    a1 = Account('Caeden')
    a1.get_name() == 'Caeden'
def test_get_balance():
    a1 = Account('Caeden')
    a1.deposit(100)
    assert a1.get_balance() == 100
