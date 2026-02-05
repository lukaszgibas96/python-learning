from twttr import shorten
from twttr import input_unify

def test_shorten():
    assert shorten("lukasz") == "lksz"

def test_get_input():
    assert input_unify("Lukasz") == "lukasz"
    assert input_unify("LuKaSz") == "lukasz"

