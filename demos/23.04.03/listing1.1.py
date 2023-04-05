#!/usr/bin/env python3
"""Calculate the area and circumference of a circle from its radius."""
import math  # statement

user_input = input("Enter the radius of your circle: ")  # expression
radius = int(user_input)

# radius = int(input("Enter the radius of your circle: "))  # expression

circumference = 2 * math.pi * radius
area = math.pi * radius**2

print(
    f"The circumference of your circle is {circumference:0.3f}, and the area is {area:0.3f}"
)  # statement
