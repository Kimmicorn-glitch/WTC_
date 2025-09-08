import pytest
from datetime import date, timedelta
import seasons

def test_age_in_min():
    today = date.today()
    yesterday = today - timedelta(days=1)
    assert seasons.age_in_min(yesterday) == 1440

def test_num_to_words():
    assert seasons.to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons.to_words(1440) == "One thousand, four hundred forty minutes"

def test_bad_date():
    with pytest.raises(SystemExit) as e:
        seasons.get_date("not-a-date")
    assert str(e.value) == "Invalid date"

def test_num_to_words_lower():
    assert seasons.num_to_words(525600) == "five hundred twenty-five thousand, six hundred"
    assert seasons.num_to_words(1440) == "one thousand, four hundred forty"
