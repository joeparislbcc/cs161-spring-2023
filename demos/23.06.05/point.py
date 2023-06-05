#!/usr/bin/env python3
from __future__ import annotations  # required for forward references

import math


class Point:
    """A point on a 2D cartesian plane."""

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x:.2f}, {self.y:.2f})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other) -> float:
        """Compute the distance between this and another Point."""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def sum(self, other) -> Point:
        return Point(self.x + other.x, self.y + other.y)
