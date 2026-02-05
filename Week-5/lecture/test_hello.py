from hello import hello

def test_default():
    assert hello("Lukasz") == "hello, Lukasz"

def test_argument():
    for name in ["Lukasz", "Adam", "Kuba"]:
        assert hello(name) == f"hello, {name}"