"""
Entry point for the Notepack app.

"""
from notepack import output
from notepack import utility
from notepack.initialize import initialize_app
from pathlib import Path


def notepack():
    output.show_welcome_message()
    initialize_app()

    category = input("Category name: ")
    notepack = input("Notepack name: ")
    open_notepack(category, notepack)
    return


def open_notepack(category, notepack):
    create_notepack(category, notepack)
    return


def create_notepack(category, notepack):
    print("Notepack")
    notepack_path = Path(utility.get_notepack_path(category, notepack))
    while True:
        try:
            print(f"Creating {notepack}...")
            notepack_path.mkdir()
            print(f"{notepack} created!")
            break
        except FileNotFoundError:
            print(f"  {category} does not exist yet.")
            create_category(category)
        except FileExistsError:
            print(f"  {notepack} already exists in {category}")
            print("  Open for editing?")
            # Open notepack for viewing.
            break
    return


def create_category(category):
    print("Category")
    category_path = Path(utility.get_category_path(category))
    try:
        print(f"  Creating {category}...")
        category_path.mkdir()
        print(f"  {category} created!")
    except FileExistsError:
        print(f"  {category} already exists.")
    return


def show_categories():
    return


def show_notepacks(category_name):
    return


