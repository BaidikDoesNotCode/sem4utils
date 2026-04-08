"""
sem4utils.functions
-------------------
Mathematical and utility functions from Semester 4 Python classwork.
"""

from typing import List, Any


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def mean(x: List[float]) -> float:
    """
    Compute the arithmetic mean of a list of numbers.

    Example:
        >>> mean([1, 2, 3])
        2.0
    """
    s = sum(x)
    return s / len(x)


def gcd(a: int, b: int) -> int:
    """
    Return the Greatest Common Divisor (GCD) of two integers
    using the Euclidean algorithm.

    Example:
        >>> gcd(48, 18)
        6
    """
    while b != 0:
        c = b
        b = a % b
        a = c
    return a


def fibonacci(n: int) -> List[int]:
    """
    Return the first n terms of the Fibonacci sequence as a list.

    Example:
        >>> fibonacci(7)
        [0, 1, 1, 2, 3, 5, 8]
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def count_occurrences(lst: list, x: Any) -> int:
    """
    Count how many times x appears in lst.

    Example:
        >>> count_occurrences([2, 3, 4, 4, 5, 6, 9, 1], 4)
        2
    """
    return sum(1 for i in lst if i == x)


def multiplication_table(n: int, up_to: int) -> List[int]:
    """
    Return the multiplication table of n up to n * (up_to - 1).

    Example:
        >>> multiplication_table(5, 4)
        [5, 10, 15]
    """
    return [n * i for i in range(1, up_to)]


def is_prime(n: int) -> bool:
    """
    Check whether a number is prime.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(9)
        False
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """
    Return the factorial of a non-negative integer.

    Example:
        >>> factorial(5)
        120
    """
    if n == 0:
        return 1
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f


def classify_number(a: int) -> str:
    """
    Classify a number as Positive/Negative Even/Odd or Zero.

    Example:
        >>> classify_number(4)
        'Positive Even'
        >>> classify_number(-3)
        'Negative Odd'
    """
    if a > 0:
        return "Positive Even" if a % 2 == 0 else "Positive Odd"
    elif a < 0:
        return "Negative Even" if a % 2 == 0 else "Negative Odd"
    else:
        return "Zero"


def is_leap_year(year: int) -> bool:
    """
    Return True if the given year is a leap year, False otherwise.

    Example:
        >>> is_leap_year(2000)
        True
        >>> is_leap_year(1900)
        False
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def classify_triangle(a: float, b: float, c: float) -> str:
    """
    Classify a triangle given its three sides.

    Returns one of: 'Equilateral Triangle', 'Isosceles Triangle',
    'Scalene Triangle', or 'Invalid Triangle'.

    Example:
        >>> classify_triangle(3, 3, 3)
        'Equilateral Triangle'
        >>> classify_triangle(3, 4, 5)
        'Scalene Triangle'
    """
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or a == c or b == c:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "Invalid Triangle"


def remove_vowels(word: str) -> str:
    """
    Return the word with all vowels removed.

    Example:
        >>> remove_vowels("education")
        'dctn'
    """
    vowels = set("AEIOUaeiou")
    return "".join(ch for ch in word if ch not in vowels)


def mystery_adder(a: float):
    """
    Return a function that adds a fixed value to its argument (closure demo).

    Example:
        >>> add_ten = mystery_adder(10)
        >>> add_ten(5)
        15
    """
    def inner(b: float) -> float:
        return a + b
    return inner
