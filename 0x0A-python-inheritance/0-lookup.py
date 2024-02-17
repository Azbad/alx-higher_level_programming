#!/usr/bin/python3
"""Module for object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes.

    Args:
        obj (object): The object to list attributes for.

    Returns:
        list: A list of attribute names available for the object.
    """
    return dir(obj)
