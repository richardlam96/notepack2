"""
Utility functions to manage (create and confirm) Paths.
"""
import shutil
from pathlib import Path
from . import config


def get_root_path():
    """Get path of where all app-created folders and files are stored."""
    return Path(config.read_root_path())


def get_path_items(path):
    """Get items in a given path in an array."""
    posix_path = Path(path)
    return [path.name for path in posix_path.glob('*')]


def create_dir_in_path(root_path, directory_name):
    """Create a new directory in the root path given."""
    if !root_path: root_path = config.read_root_path()
    new_dir_path = Path(root_path).joinpath(directory_name)
    new_dir_path.mkdir()
    return new_dir_path


def create_template_copy(root_path, filename):
    """Copy the given file's template to the root path given."""
    return shutil.copy(config.read_template_path(filename), Path(root_path))



