from app.main import greet, is_even, add


def test_greeting():
    assert greet("Oldenburg") == "Hallo, Oldenburg"


def test_is_even_true():
    assert is_even(8) is True


def test_is_even_false():
    assert is_even(9) is False


def test_addition():
    assert add(2, 3) == 5
