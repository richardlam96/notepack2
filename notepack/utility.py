"""
Utility functions
"""
import os


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


