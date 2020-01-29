"""
Entry point for the Notepack app.

"""
from notepack import config
from notepack import output
from notepack import utility
from notepack.initialize import initialize_app


def notepack():
    output.show_welcome_message()
    initialize_app()

    print("Categories:")
    show_categories()


def show_categories():
    utility.list_path(config.DEFAULT_FOLDERS["tickets"])
    return


def create_category(name):
    return


def show_notepacks(category_name):
    category_path = f"{config.DEFAULT_FOLDERS['tickets']}/{category_name}"
    utility.list_path(category_path)
    return


def create_notepack(name):
    return


