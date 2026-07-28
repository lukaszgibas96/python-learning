from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(2)
    assert jar.size == 7

    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(20)
    assert jar.size == 0
    
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)
    assert jar.size == 0
 



def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert jar.size == 11

    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    assert jar.size == 0

    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    assert jar.size == 0

