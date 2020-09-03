# Task 1
# Create your own implementation of a built-in function enumerate, named `with_index`,
# which takes two parameters: `iterable` and `start`, default is 0. Tips:
# see the documentation for the enumerate function


# def with_index(i):
#     a = [10, 20, 30, 40]
#     for i in enumerate(a, 10):
#         print(i)
#
#
# with_index(5)


# Task 2
# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step. Tips:
# See the documentation for `range` function


def in_range(start, end, step):
    a = range(start, end, step)
    for i in enumerate(a, 1):
        print(i)


in_range(0, 100, 5)






