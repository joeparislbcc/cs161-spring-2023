#!/usr/bin/env python3


class Student:
    school = "Linn-Benton Community College"

    def __init__(self, name: str, major: str):
        self.name = name
        self.major = major

    def __str__(self) -> str:
        return f"{self.name} is a {self.major} major at {self.school}."

    def __repr__(self) -> str:
        return f"Student({self.name}, {self.major})"
