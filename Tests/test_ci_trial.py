# This test helps verify that Travis CI was set up correctly.
def dummy_foo():
    return True


def foo_test():
    assert dummy_foo() is True

