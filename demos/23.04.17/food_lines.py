#!/usr/bin/env python3
import pathlib

cwd = pathlib.Path(__file__).parent
input_file = cwd / "in.txt"
with open(input_file, mode="r", encoding="UTF-8") as in_file:
    num_lines, num_people = (int(num) for num in in_file.readline().split())
    food_lines = [int(num) for num in in_file.readline().split()]

for _ in range(num_people):
    shortest_line = min(food_lines)
    shortest_idx = food_lines.index(shortest_line)
    print(food_lines[shortest_idx])
    food_lines[shortest_idx] += 1
