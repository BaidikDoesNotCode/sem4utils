"""
sem4utils
=========
A Python utility package based on Semester 4 classwork covering:
- String operations
- List operations
- Mathematical functions

Usage
-----
    from sem4utils.functions import gcd, fibonacci, is_prime
    from sem4utils.strings import format_certificate, replace_substring
    from sem4utils.lists import sort_list, count_occurrences
"""

from .functions import (
    add,
    mean,
    gcd,
    fibonacci,
    count_occurrences,
    multiplication_table,
    is_prime,
    factorial,
    classify_number,
    is_leap_year,
    classify_triangle,
    remove_vowels,
    mystery_adder,
)

from .strings import (
    check_starts_with,
    check_ends_with,
    is_all_upper,
    is_all_lower,
    is_all_space,
    to_title_case,
    concatenate_words,
    count_char,
    find_char,
    replace_substring,
    is_substring,
    format_certificate,
)

from .lists import (
    get_element,
    slice_list,
    update_element,
    replace_slice,
    concatenate_lists,
    add_element,
    insert_element,
    extend_list,
    remove_by_index,
    remove_by_value,
    sort_list,
    list_from_string,
    join_list_to_string,
    nested_get,
)

__version__ = "0.1.0"
__author__ = "Baidik"
__all__ = [
    # functions
    "add", "mean", "gcd", "fibonacci", "count_occurrences",
    "multiplication_table", "is_prime", "factorial", "classify_number",
    "is_leap_year", "classify_triangle", "remove_vowels", "mystery_adder",
    # strings
    "check_starts_with", "check_ends_with", "is_all_upper", "is_all_lower",
    "is_all_space", "to_title_case", "concatenate_words", "count_char",
    "find_char", "replace_substring", "is_substring", "format_certificate",
    # lists
    "get_element", "slice_list", "update_element", "replace_slice",
    "concatenate_lists", "add_element", "insert_element", "extend_list",
    "remove_by_index", "remove_by_value", "sort_list", "list_from_string",
    "join_list_to_string", "nested_get",
]
