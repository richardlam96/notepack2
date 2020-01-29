"""
Entry point for the Notepack app.

"""
from notepack import output
from notepack import utility
from notepack.initialize import initialize_app


def notepack():
    output.show_welcome_message()
    initialize_app()

    print("Categories:")
    show_categories()


def show_categories():
    return


def create_category(name):
    return


def show_notepacks(category_name):
    return


def create_notepack(name):
    return


