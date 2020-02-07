"""
Entry point for the Notepack app.

"""
from notepack import output
from notepack import utility
from notepack import initialize
from notepack.actions import category


def notepack():
    """Begin the app with the main console

    Includes printing messages and checking for required folders and files.
    """
    output.print_welcome_message()
    initialize.confirm_required_folders()
    initialize.confirm_required_files()

    # Start the main notepack console.
    print("What would you like to do?")
    while True:
        command = input("> ").split()
        if not command: continue

        action = command[0]
        if action == 'quit': break
        if action == 'search': enter_search_console()

        continue
    return


def enter_search_console():
    """Search console
    
    One type of console used to search and open a notepack.
    """
    print("Search Console")
    while True:
        command = input("search> ").split()
        if not command: continue
        if command[0] == 'quit': break

        category_name = confirm_category_console(command[0])
        notepack = confirm_notepack_console(category_name, command[1])

        print(f"Opening {notepack} in {category_name}")
    return


def confirm_category_console(category_name):
    """Sub-console to confirm existing or create a new category"""
    while True:
        category_path = utility.get_category_path(category_name)
        print(f"'{category_name}' does not exist.")
        print("Choose an existing category or create 'new':")
        output.print_categories()
        new_category_name = input("category or 'new'> ")

        if new_category_name == 'new': 
            category.create_category(category_path)
            break 
        category_name = new_category_name

    return category_path


def confirm_notepack_console(category_name, notepack):
    """Sub-console to confirm existing or create a new notepack"""
    while not notepack in utility.get_notepacks(category_name):
        print(f"'{notepack}' NOT found!")
        print("Choose an existing notepack or creaste 'new':")
        output.print_notepacks(category_name)
        new_notepack = input(f"{category_name}>notepack or 'new'> ")
        if new_notepack == 'new': 
            print(f"Creating new notepack called '{notepack}'...")
            notepack = new_notepack
            break
    return notepack


def pick_from_list(items, prompt="> "):
    while True:
        requested_item = input(prompt)
        if requested_item in items:
            break
        else:
            print(f"'{requested_item}' is not available.")
            print(f"Try one of these: {items}")

    return requested_item


