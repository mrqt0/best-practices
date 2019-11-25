"""Implement delayed or weak assert.

There must be some kind of memory or global state to remember the failures.
There are several options:
- Global variable
- Nonlocal variable (must be foudn through call stack somehow)
- Callable class or object

"""

import types


class Checker:
    """Option 1: Callable object."""

    def __init__(self):
        self._failures = list()

    def __call__(self, expression, message, fatal=False):
        """Actual check function."""
        if not expression:
            self._failures.append(message)

    def reset(self):
        """Reset lsit of failures for next test."""
        self._failures = list()

    def evaluate(self):
        """Evaluate failures."""
        for failure in self._failures:
            print(failure)


class Checker2:
    """Option 2: Callable class."""

    _failures = list()

    def __new__(cls, expression, message, fatal=False):
        """Actual check function."""
        if not expression:
            cls._failures.append(message)

    @classmethod
    def reset(cls):
        """Reset lsit of failures for next test."""
        cls._failures = list()

    @classmethod
    def evaluate(cls):
        """Evaluate failures."""
        for failure in cls._failures:
            print(failure)


def check3(expression, message, fatal=False):
    """Option 3: Closure"""
    failures = list()
    def check(expression, message):
        if not expression:
            failures.append(message)
    # FIXME: how do we acces failures?
    return check


wavetest = types.SimpleNamespace()
wavetest.check1 = Checker()
wavetest.check2 = Checker2


def test1():
    """Test using the first option."""
    wavetest.check1(0 == 1, "Zero is not one")
    wavetest.check1("a" == "b", "A is not B")


def test2():
    """Test using the second option."""
    wavetest.check2(0 == 1, "Zero is not one")
    wavetest.check2("a" == "b", "A is not B")


def main():
    wavetest.check1.reset()
    test1()
    wavetest.check1.evaluate()

    wavetest.check2.reset()
    test2()
    wavetest.check2.evaluate()


if __name__ == "__main__":
    main()


