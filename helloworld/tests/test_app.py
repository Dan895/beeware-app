from helloworld.app import greetting


def test_name():
    """If a name is provided, the greetting includs the name"""

    assert greetting("Alice") == "Hello, Alice"


def test_empty():
    """If a name is not provided, a generic greetting is provided"""
    assert greetting("") == "Hello, stranger"

# This defines a test for a specific user


def test_brutus():
    """If the name is Brutus, a special greeting is provided"""
    assert greetting("Brutus") == "BeeWare the IDEs of Python!"
