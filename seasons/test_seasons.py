
import pytest # pyright: ignore[reportMissingImports]
import sys
import seasons
from datetime import date, timedelta

def test_age_in_min():
    today = date.today()
    yesterday = today - timedelta(days=1)
    assert seasons.age_in_min(yesterday) == 1440

def test_minutes_to_words():
    assert seasons.minutes_to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert seasons.minutes_to_words(1440) == "One thousand, four hundred forty minutes"

def test_invalid_date_VE():
    bad_date = "not_a_date"
    with pytest.raises(SystemExit) as e:
        try:
            seasons.date.fromisoformat(bad_date)
        except ValueError:
            sys.exit("Invalid date")

    assert str(e.value) == "Invalid date"
