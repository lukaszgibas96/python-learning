from seasons import convert
from datetime import date

def test_convert_one_year():
    assert convert("2026-07-27", date(2027,7,27)) == "five hundred twenty-five thousand, six hundred"
def test_convert_one_day():
    assert convert("2026-07-27", date.fromisoformat("2026-07-28")) == "one thousand, four hundred forty"
def test_convert_same_day():
    assert convert("2026-07-27", date.fromisoformat("2026-07-27")) == "zero"    
