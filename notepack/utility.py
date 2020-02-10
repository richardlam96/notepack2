"""
Utility functions

Functions using the pathlib library and the config variables set in the app.
These functions will do most of the error handling as well.
"""
from pathlib import Path
from notepack import config


def get_notepacks(category):
    """List notepacks existing in given category."""
    return get_path_items(get_category_path(category))


def get_categories():
    """List categories in the path from config.  """
    return get_path_items(config.DEFAULT_FOLDERS['tickets'])


def get_notepack_path(category_path, notepack_name):
    """Build path for a notepack."""
    return category_path.joinpath(notepack_name)


def get_category_path(category_name):
    """Build path for a category."""
    return get_root_path().joinpath(category_name)


def get_root_path():
    return Path(f"{config.DEFAULT_FOLDERS['tickets']}")


def get_template_path(name):
    return Path(f"{config.DEFAULT_TEMPLATES[name]}")


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


def get_path_items(path):
    """Get items in a given path in an array."""
    posix_path = Path(path)
    return [path.name for path in posix_path.glob('*')]


def create_path(path):
    path.mkdir()
    return
