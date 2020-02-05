"""
Actions for notepacks: Create, List, Open, Use?, Delete.
"""
from pathlib import Path
from notepack import utility


def open_notepack(category, notepack):
    return


def create_notepack(category, notepack):
    notepack_path = utility.get_notepack_path(category, notepack)
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



def show_notepacks(category_name):
    return
