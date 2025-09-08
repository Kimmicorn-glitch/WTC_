from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("AEIOU") == ""

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_mixed():
    assert shorten("HEllo") == "Hll"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("C@T") == "C@T"
    assert shorten("hello!") == "hll!"
