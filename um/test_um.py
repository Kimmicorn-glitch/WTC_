import pytest
from um import count

def test_um():
    assert count("Hello, um, world") == 1
    assert count("um") == 1

def test_case():
    assert count("UM, um, Um") == 3
    assert count("uM") == 1

def test_not_in_word():
    assert count("Yummy") == 0
    assert count("dummy") == 0
    assert count("alumni") == 0

def test_punctuation():
    assert count("um!") == 1
    assert count("um?") == 1
    assert count("..um?") == 1
