from bank import value

def test_value_0():
    assert value("hello") == 0
def test_value_20():
    assert value("hi") == 20
def test_value_100():
    assert value("bye") == 100

    
    