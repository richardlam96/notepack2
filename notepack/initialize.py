"""
Initialize Functions

Initialize any files and folders that are required for the app to work
properly.

This can probably later be moved to another exiting file. Pointless to have it
seperate at this point.
"""
from notepack import config
from notepack import utility


def confirm_required_folders():
    """Create top-level folders if needed."""
    print("Checking required folders...")
    utility.paths_in_dictionary_exists(config.DEFAULT_FOLDERS)
    return


def confirm_required_files():
    """Ask to create required files if needed."""
    print("Checking required templates...")
    utility.paths_in_dictionary_exists(config.DEFAULT_FILES)
    return



