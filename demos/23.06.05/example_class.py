#!/usr/bin/env python3
"""An example of a Python class."""


class ExampleClass:
    """A very basic example of a Python class."""

    def __init__(self, param1: int, param2: int):
        """Initialize the example object.

        The init method never has a return value.
        """
        self.attribute1 = param1
        self.attribute2 = param2

    def __str__(self) -> str:
        """Create a string representation of the example object .

        The return value of the str method should be a reasonable representation
        of the object and is meant to be understood by users.
        """
        return f"{self.attribute1}, {self.attribute2}"

    def __repr__(self) -> str:
        """Create a string representation of the example object suitable for debugging.

        The return value of the repr method is used for debugging purposes and
        often looks like a call to the object's init method.
        """
        return f"Example(param1={self.attribute1}, param2={self.attribute2})"
