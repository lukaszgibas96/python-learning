import pytest
from working import convert


def test_convert_1():
    assert convert("9 AM to 8 PM") == "09:00 to 20:00"
def test_convert_2():
    assert convert("9:00 AM to 8:00 PM") == "09:00 to 20:00"
def test_convert_3():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
def test_convert_4():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
def test_error_convert_1():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")