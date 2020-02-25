"""
Initialize Functions

Initialize any files and folders that are required for the app to work
properly.

This can probably later be moved to another exiting file. Pointless to have it
seperate at this point.
"""
from notepack import config
from notepack import logger


def confirm_required_folders():
    """Create top-level folders if needed."""
    logger.log("Checking required folders...")
    paths_in_dictionary_exists(config.DEFAULT_FOLDERS)
    return


def confirm_required_files():
    """Ask to create required files if needed."""
    logger.log("Checking required templates...")
    paths_in_dictionary_exists(config.DEFAULT_TEMPLATES)
    return


def paths_in_dictionary_exists(dictionary):
    """Check if all paths in a dictionary exist."""
    for name, path in dictionary.items():
        if path_exists(path):
            logger.log(f"{name} path exists.", 1)
        else:
            logger.log(f"{name} path MISSING.", 1)
    return



