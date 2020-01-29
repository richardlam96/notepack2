"""
Entry point for the Notepack app.

"""
from notepack import output
from notepack import utility
from notepack.initialize import initialize_app


def notepack():
    output.show_welcome_message()
    initialize_app()

    category = input("Category name: ")
    notepack = input("Notepack name: ")
    open_notepack(category, notepack)
    return


def open_notepack(category, notepack):
    create_category(category)
    create_notepack(notepack)
    return


def create_category(category):
    print("Category")
    category_path = get_category_path(category)
    if utility.path_exists(category_path):
        print(f"  {category} already exists")
    else:
        print(f"  Creating {category}")
    return


def create_notepack(category, notepack):
    print("Notepack")
    notepack_path = get_notepack_path(category, notepack)
    if utility.path_exists(notepack_path):
        print(f"  {notepack} already exists in {category}")
    else:
        print(f"  Creating {notepack} in {category}")
    return


def show_categories():
    return


def show_notepacks(category_name):
    return


