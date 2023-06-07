#!/usr/bin/env python3
from example_class import ExampleClass

ex1 = ExampleClass(37, 42)  # __init__ is called here
ex2 = ExampleClass(1, 2)  # __init__ is called here

print(ex1)
print(repr(ex1))
print(f"{ex1!r}")  # alternate syntax using the !r conversion flag
