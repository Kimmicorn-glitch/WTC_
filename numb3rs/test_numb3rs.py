import pytest
from numb3rs import validate


def test_parts():
    assert validate("255.1.2.3") == True
    assert validate("256.02.1.20") == False
    assert validate("1000.100.10.1") == False

def test_negative():
    assert validate("-255.01.1.2") == False
    assert validate("0.25.-2.255") == False
    assert validate("1.2.3.4") == True


def test_isdigit():
    assert validate("cat.dog.pig.rat") == False
    assert validate("192.1.2.cat") == False

def test_len_parts():
    assert validate("1.2.3.4.5") == False
    assert validate("1.2") == False

def test_in_range():
    assert validate("0.02.12.3") == False
    assert validate("0.00.00.0") == False

def test_int():
    assert validate("257.12.298.999") == False

