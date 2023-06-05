#!/usr/bin/env python3
from student import Student

students = [
    Student("Victoria Gregorowicz", "Computer Science"),
    Student("Marty Spadeck", "Basket Weaving"),
    Student("Jemmie Stonelake", "Basket Weaving"),
    Student("Alfred Meckiff", "Computer Science"),
    Student("Kiley Turbat", "Business"),
]

for student in students:
    print(student)

for student in students:
    print(student.name)

Student.school = "the school of hard knocks"

for student in students:
    print(student)
