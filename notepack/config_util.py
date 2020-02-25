"""
Utility functions for accessing and editing config elements so there is no need
to import the config module everywhere.
"""
from pathlib import Path
from notepack import config


def read_template_path(filename):
    """Get the configured path where a template is."""
    return config.DEFAULT_TEMPLATES[filename]


def read_dir_names(entity_key):
    """Get the list of directory names from an Entity's config."""
    return config.ENTITIES[entity_key]["directories"]


def read_file_names(entity_key):
    """Get the list of file names from an Entity's config."""
    return config.ENTITIES[entity_key]["files"]


def read_entity_config(entity_key):
    """Get the config object for an Entity."""
    return config.ENTITIES[entity_key]


def read_entities():
    """Return a list of Entities in the config."""
    return config.ENTITIES.keys()


def read_entity(index):
    """Get nth Entity."""
    return config.ENTITIES.keys()[index]


def read_root_path():
    """
    Get path string of where all app-created folders and files are stored.
    """
    return config.DEFAULT_FOLDERS['tickets']





