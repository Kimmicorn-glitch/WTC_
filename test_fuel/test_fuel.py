import pytest
from fuel import convert,gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("99/100") == 99
    assert convert("0/1") == 0

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
<<<<<<< HEAD
=======
    
>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"

def test_convert_negative():
<<<<<<< HEAD
    import pytest
    from fuel import convert
=======
>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562

    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ValueError):
        convert("1/-2")