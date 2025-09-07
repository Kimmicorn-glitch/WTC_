from bank import value

def test_hello():
<<<<<<< HEAD
    assert value("Hello") == 0
=======
    assert value("hello") == 0
>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562
    assert value("hello") == 0
    assert value("hello there") == 0

def test_h_only():
<<<<<<< HEAD
    assert value("Hey") == 20
    assert value("hi") == 20
    assert value("how are you") == 20
=======
    assert value("hey") == 20
    assert value("hi") == 20
    assert value("howdy") == 20
>>>>>>> 4e8093f5474ca1ab25b9cd33131df1c208bf3562

def test_other():
    assert value("greetings") == 100
    assert value("good day") == 100
    assert value("im older than google") == 100
