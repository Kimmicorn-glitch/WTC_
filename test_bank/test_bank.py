from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello") == 0
   # assert value("hello there") == 0

def test_h_only():
    assert value("hey") == 20
    assert value("hi") == 20
    assert value("howdy") == 20

def test_other():
    assert value("greetings") == 100
    assert value("good day") == 100
    assert value("im older than google") == 100
