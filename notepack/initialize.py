"""
Initialize Functions

Initialize any files and folders that are required for the app to work
properly.
"""
import os
from notepack import config


def initialize_app():
    """Check for required app files and initialize if needed."""
    confirm_required_folders()
    confirm_required_files()
    return


def confirm_required_folders():
    """Create top-level folders if needed."""
    print("Checking required folders...")
    
    for name, path in config.DEFAULT_FOLDERS.items():
        if path_exists(path):
            print(f"\t{name} folder exists.")
        else:
            print(f"\t{name} folder MISSING.")

    return


def confirm_required_files():
    """Ask to create required files if needed."""
    print("Checking required templates...")

    for name, path in config.DEFAULT_FILES.items():
        if path_exists(path):
            print(f"\t{name} file found.")
        else: 
            print(f"\t{name} file MISSING.")

    return


def path_exists(path):
    """Check if the given path exists."""
    return os.path.exists(path)


