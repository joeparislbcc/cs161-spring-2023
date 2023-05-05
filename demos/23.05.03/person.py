#!/usr/bin/env python3
class Person:
    def __init__(self, name: str) -> None:
        print("Inside Person.__init__")
        self.name = name


person1 = Person("Joe")
person2 = Person("Autumn")

print(person1.name)
print(person2.name)
pass
