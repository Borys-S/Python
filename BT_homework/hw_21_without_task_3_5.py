"""
Task 1

from typing import Optional
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:

    Returns  x ^ exp

    >>> to_power(2, 3) == 8
    True

    >>> to_power(3.5, 2) == 12.25
    True

    >>> to_power(2, -1)
    ValueError: This function works only with exp > 0.

"""


# def to_power(x, exp):
#     if exp < 0:
#         return r"ValueError: This function works only with exp > 0."
#     elif exp == 0:
#         return 1
#     return to_power(x, exp - 1) * x
#
#
# print(to_power(2, -1))

"""
Task 2

from typing import Optional
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    
    Checks if input string is Palindrome
    >>> is_palindrome('mom')
    True

    >>> is_palindrome('sassas')
    True

    >>> is_palindrome('o')
    True
    
    pass
"""

# def is_palindrome(is_this_a_palindrome):
#     if len(is_this_a_palindrome) <= 1:
#         return True
#     elif is_this_a_palindrome[0] != is_this_a_palindrome[-1]:
#         return False
#     return is_palindrome(is_this_a_palindrome[1:-1])
#
#
# print(is_palindrome(input()))

"""
Task 3

from typing import Optional
def mult(a: int, n: int) -> int:
    
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    ValueError("This function works only with postive integers")
"""

pass

"""
Task 4

def reverse(input_str: str) -> str:

    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True  
"""

# def reverse(string):
#     if len(string) == 1:
#         return string
#     elif len(string) == 0:
#         return string
#     return reverse(string[1:]) + string[0]
#
# print(reverse(input()))

"""
Task 5

def sum_of_digits(digit_string: str) -> int:
    
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    ValueError("input string must be digit string")
"""

pass
