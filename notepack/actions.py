"""
Basically CRUD actions to be performed on notepacks and categories (parent
notepacks).
"""
from pathlib import Path
from notepack import utility
from notepack import actions


def open_notepack(category, notepack):
    return


def create_notepack(category, notepack):
    notepack_path = Path(utility.get_notepack_path(category, notepack))
    while True:
        try:
            print(f"Creating {notepack}...")
            notepack_path.mkdir()
            print(f"{notepack} created!")
            break
        except FileExistsError:
            print(f"  {notepack} already exists in {category}")
            print("  Open for editing?")
            # Open notepack for viewing.
            break
    return


def delete_notepack(category, notepack):
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


