"""
Utility functions
"""
import os
from notepack import config


def get_notepack_path(category_name, notepack_name):
    """Build path for a notepack."""
    category_path = get_category_path(category_name)
    return f"{category_path}/{notepack_name}"


def get_category_path(category_name):
    """Build path for a category."""
    return f"{config.DEFAULT_FOLDERS['tickets']}/{category_name}"


def list_categories():
    """List categories in the path from config."""
    list_path(config.DEFAULT_FOLDERS['tickets'])
    return


def paths_in_dictionary_exists(dictionary):
    """Check if all paths in a dictionary exist."""
    for name, path in dictionary.items():
        if path_exists(path):
            print(f"\t{name} path exists.")
        else:
            print(f"\t{name} path MISSING.")
    return


def path_exists(path):
    """Check if the given path exists."""
    return os.path.exists(path)


def list_path(path):
    """List items in a given path."""
    return os.listdir(path)


