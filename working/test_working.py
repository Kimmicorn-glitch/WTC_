import pytest
from working import convert

def test_negative():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_with_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"

def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

def test_edge_cases():
    assert convert("1 AM to 1 PM") == "01:00 to 13:00"
    assert convert("11 PM to 11 AM") == "23:00 to 11:00"

def test_invalid_format():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")

def test_bad_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 10:61")

def test_missing_meridiem():
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")

def test_missing_to():
    with pytest.raises(ValueError):
        convert("9:00 AM- 5:00 PM")

