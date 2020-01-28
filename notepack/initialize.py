"""
Initialize Functions

Initialize any files and folders that are required for the app to work
properly.
"""
import os


def initialize_app():
    """Check for required app files and initialize if needed."""
    if not path_exists("./tickets"):
        print("Initial files and folders not found.")
        action = input("Create? (Y/n): ")
        if action == 'n':
            print("WARNING: tickets/ path was not created!")
            return
        os.mkdir("./tickets")

    print(os.listdir("./tickets"))


def confirm_required_folders():
    """Create top-level folders if needed."""
    return


def confirm_required_files():
    """Ask to create required files if needed."""
    return


def path_exists(path):
    """Check if the given path exists."""
    return os.path.exists(path)


