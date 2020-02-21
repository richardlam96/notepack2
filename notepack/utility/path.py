"""
Utility functions to manage (create and confirm) Paths.
"""
from . import config


def get_root_path():
    """Get path of where all app-created folders and files are stored."""
    return Path(config.get_root())


def get_path_items(path):
    """Get items in a given path in an array."""
    posix_path = Path(path)
    return [path.name for path in posix_path.glob('*')]


def create_dir_in_path(path, directory_name):
    return


def copy_file_to_path(path, filename):
    return


