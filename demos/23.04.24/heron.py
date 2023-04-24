#!/usr/bin/env python3


import math


def get_vertex(count: str) -> tuple[float, float]:
    """Get the x and y values for a vertex in the triangle.

    Args:
        count (str): Description (count) of the vertex to be entered.

    Returns:
        tuple[float, float]: A 2-tuple representing the x- and y-coordinate.
    """
    x = float(input(f"Please enter the x-coordinate for the {count} vertex: "))
    y = float(input(f"Please enter the y-coordinate for the {count} vertex: "))

    return x, y


def get_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Compute the distance between two points on a plane.

    Args:
        x1 (float): The x-coordinate of the first point.
        y1 (float): The y-coordinate of the first point.
        x2 (float): The x-coordinate of the second point.
        y3 (float): The y-coordinate of the second point.

    Returns:
        float: The distance between the two points.
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def heron(a: float, b: float, c: float) -> float:
    """_summary_

    Args:
        a (float): _description_
        b (float): _description_
        c (float): _description_

    Returns:
        float: _description_
    """
    s = 0.5 * (a + b + b)
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    """Find the area of a triangle given its three vertices."""
    # 1. Prompt for the three vertices of the triangle.
    x1, y1 = get_vertex("first")
    x2, y2 = get_vertex("second")
    x3, y3 = get_vertex("third")

    # write a function to test the vertices and see if they form a triangle

    # 2. Find the length of each side.
    a = get_distance(x1, y1, x2, y2)
    b = get_distance(x2, y2, x3, y3)
    c = get_distance(x1, y1, x3, y3)

    # 3. Find the area using Heron's Formula.
    area = heron(a, b, c)
    print(f"The area of the triangle is {area:.2f} square units.")


if __name__ == "__main__":
    main()
