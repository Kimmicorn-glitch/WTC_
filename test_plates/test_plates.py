from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCD1234") == False
    assert is_valid("ABC123") == True

def test_starts_with_letter():
    assert is_valid("A") == False
    assert is_valid("1ABC") == False
    assert is_valid("12ABC") == False
    assert is_valid("A1BC") == False
    assert is_valid("AB123") == True
    assert is_valid("CS50") == True

def test_numbers_rules():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50A") == False

def test_alphanumeric_only():
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("HELLO") == True

def test_must_start_with_two_letters():
    assert is_valid("1A") == False
    assert is_valid("22") == False
    assert is_valid("5T") == False
    assert is_valid("AB") == True
