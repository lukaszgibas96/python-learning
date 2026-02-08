from fuel import convert, gauge

def test_convert_1():
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("6/8") == 75

def test_gauge_1():
    assert gauge(1) == "E"
def test_gauge_2():
    assert gauge(0) == "E"
def test_gauge_3():
    assert gauge(99) == "F"
def test_gauge_4():
    assert gauge(50) == "50%"




