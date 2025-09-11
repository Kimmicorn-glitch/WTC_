import pytest
from project import to_Fahrenheit, to_Kelvin

def test_to_Fahrenheit():
    assert to_Fahrenheit(0) == 32
    assert to_Fahrenheit(100) == 212
    assert to_Fahrenheit(-40) == -40
    assert round(to_Fahrenheit(25), 2) == 77.00

def test_to_Kelvin():
    assert to_Kelvin(0) == 273.15
    assert to_Kelvin(100) == 373.15
    assert round(to_Kelvin(25),2) == 298.15

def test_to_Fahrenheit_invalid():
    with pytest.raises(TypeError):
        to_Fahrenheit("cat")

def test_to_Kelvin_invalid():
    with pytest.raises(TypeError):
        to_Kelvin("dog")

