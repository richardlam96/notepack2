"""
Utility functions
"""
from pathlib import Path
from notepack import config


def list_categories():
    """List categories in the path from config."""
    return list_path(config.DEFAULT_FOLDERS['tickets'])


def list_notepacks(category):
    """List notepacks existing in given category."""
    return list_path(get_category_path(category))


def get_notepack_path(category_name, notepack_name):
    """Build path for a notepack."""
    category_path = get_category_path(category_name)
    return f"{category_path}/{notepack_name}"


def get_category_path(category_name):
    """Build path for a category."""
    return f"{config.DEFAULT_FOLDERS['tickets']}/{category_name}"


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
    return Path(path).exists()


def list_path(path):
    """List items in a given path."""
    posix_path = Path(path)
    return [path.name for path in posix_path.glob('*')]


