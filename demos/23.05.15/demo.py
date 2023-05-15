# some_var = 27


# def some_func(param1=123, param2="Python"):
#     for key, val in locals().items():
#         print(f"key {key}: {val}")
#     some_var = some_var + 1
#     print(some_var)


# some_func(123456, "spam")


# def append_to(element, to=[]):
#     to.append(element)
#     return to


# my_list = append_to(12)
# print(my_list)
# # [12]

# my_other_list = append_to(42)
# print(my_other_list)
# # [12, 42]


# def my_sum(*args):
#     result = 0
#     # Iterating over the Python args tuple
#     for x in args:
#         result += x
#     return result


# print(my_sum(1))
# print(my_sum(1, 2))
# print(my_sum(1, 2, 3, 4))
# print(my_sum(1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6, 56, 7, 5, 56, 23, 45, 4))


# def concatenate(**kwargs):
#     result = ""
#     # Iterating over the Python kwargs dictionary
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#     return result


# print(concatenate(a="Programming", b="is", c="fun!"))


def my_weird_func(first_param, ham=37, *args, **kwargs):
    """This is a weird function."""
    print(first_param)
    print(ham)
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    print(result)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_weird_func(1, 2, 3, 4, 5, a="Programming", b="is", c="fun!")

print(my_weird_func.__doc__)
print(my_weird_func.__dict__)
print(my_weird_func.__annotations__)
print(my_weird_func.__code__)
