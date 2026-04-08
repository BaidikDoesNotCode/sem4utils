"""
sem4utils.strings
-----------------
String operation utilities from Semester 4 Python classwork.
"""


def check_starts_with(string: str, prefix: str) -> bool:
    """Check if a string starts with the given prefix."""
    return string.startswith(prefix)


def check_ends_with(string: str, suffix: str) -> bool:
    """Check if a string ends with the given suffix."""
    return string.endswith(suffix)


def is_all_upper(string: str) -> bool:
    """Check if all characters in a string are uppercase."""
    return string.isupper()


def is_all_lower(string: str) -> bool:
    """Check if all characters in a string are lowercase."""
    return string.islower()


def is_all_space(string: str) -> bool:
    """Check if all characters in a string are whitespace."""
    return string.isspace()


def to_title_case(string: str) -> str:
    """Convert a string to title case (capitalize first letter of each word)."""
    return string.title()


def concatenate_words(*words: str, sep: str = " ") -> str:
    """Concatenate multiple words with a separator (default: space)."""
    return sep.join(words)


def count_char(string: str, char: str) -> int:
    """Count how many times a character/substring appears in the string."""
    return string.count(char)


def find_char(string: str, char: str) -> int:
    """Find the first index of a character/substring. Returns -1 if not found."""
    return string.find(char)


def replace_substring(string: str, old: str, new: str) -> str:
    """Replace all occurrences of old substring with new substring."""
    return string.replace(old, new)


def is_substring(substring: str, string: str) -> bool:
    """Check if substring is present in string."""
    return substring in string


def format_certificate(name: str, semester: int, department: str) -> str:
    """
    Generate a formatted certificate string.

    Example:
        >>> format_certificate("S", 1, "Statistics")
        'This is to certify that Ms S belongs to Semester 1 of the Statistics department.'
    """
    return f"This is to certify that Ms {name} belongs to Semester {semester} of the {department} department."
