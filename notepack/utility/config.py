"""
Utility functions for accessing and editing config elements so there is no need
to import the config module everywhere.
"""
from pathlib import Path
from notepack import config


def get_directory_names(entity_key):
    """Get the list of directory names from an Entity's config."""
    return config.ENTITIES[entity_key]["directories"]


def get_file_names(entity_key):
    """Get the list of file names from an Entity's config."""
    return config.ENTITIES[entity_key]["files"]


def get_config(entity_key):
    """Get the config object for an Entity."""
    return config.ENTITIES[entity_key]


def get_entities():
    """Return a list of Entities in the config."""
    return config.ENTITIES.keys()


def get_entity(index):
    """Get nth Entity."""
    return config.ENTITIES.keys()[index]



