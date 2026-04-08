"""
sem4utils.lists
---------------
List operation utilities from Semester 4 Python classwork.
"""

from typing import Any


def get_element(lst: list, index: int) -> Any:
    """Return the element at the given index (supports negative indexing)."""
    return lst[index]


def slice_list(lst: list, start: int = None, end: int = None) -> list:
    """Return a slice of the list from start to end."""
    return lst[start:end]


def update_element(lst: list, index: int, value: Any) -> list:
    """Update a list element at the given index. Returns the modified list."""
    lst[index] = value
    return lst


def replace_slice(lst: list, start: int, end: int, new_elements: list) -> list:
    """Replace a slice of the list with new elements. Returns the modified list."""
    lst[start:end] = new_elements
    return lst


def concatenate_lists(*lists: list) -> list:
    """Concatenate multiple lists into one."""
    result = []
    for lst in lists:
        result += lst
    return result


def add_element(lst: list, element: Any) -> list:
    """Append an element to the end of the list. Returns the modified list."""
    lst.append(element)
    return lst


def insert_element(lst: list, index: int, element: Any) -> list:
    """Insert an element at the given index. Returns the modified list."""
    lst.insert(index, element)
    return lst


def extend_list(lst: list, other: list) -> list:
    """Extend a list by appending all elements of another list."""
    lst.extend(other)
    return lst


def remove_by_index(lst: list, index: int = -1) -> Any:
    """
    Remove and return the element at the given index (default: last element).

    Example:
        >>> remove_by_index([1, 5, 6, 9], 0)  # removes first element
        1
    """
    return lst.pop(index)


def remove_by_value(lst: list, value: Any) -> list:
    """Remove the first occurrence of a value from the list."""
    lst.remove(value)
    return lst


def sort_list(lst: list, reverse: bool = False) -> list:
    """Return a new sorted list."""
    return sorted(lst, reverse=reverse)


def list_from_string(string: str) -> list:
    """
    Create a list of characters from a string.

    Example:
        >>> list_from_string('python')
        ['p', 'y', 't', 'h', 'o', 'n']
    """
    return list(string)


def join_list_to_string(lst: list, sep: str = "") -> str:
    """
    Concatenate elements of a list into a string.

    Example:
        >>> join_list_to_string(['p', 'y', 't', 'h', 'o', 'n'])
        'python'
    """
    return sep.join(lst)


def nested_get(nested_list: list, *indices: int) -> Any:
    """
    Access an element in a nested list using multiple indices.

    Example:
        >>> nested_get([['A', 'F', 80], ['B', 'F', 70]], 1, 2)
        70
    """
    result = nested_list
    for i in indices:
        result = result[i]
    return result
