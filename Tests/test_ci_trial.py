# This test helps verify that Travis CI was set up correctly.
def dummy_foo():
    return True


def test_foo():
    assert dummy_foo() is True

