"""
Entry point for the Notepack app.

"""
from notepack import output
from notepack import utility
from notepack import initialize
from notepack.actions import category


def notepack():
    output.print_welcome_message()
    initialize.confirm_required_folders()
    initialize.confirm_required_files()

    # Start of the notepack "terminal".
    print("What would you like to do?")
    while True:
        # Validate there is input.
        command = input("> ").split()
        if not command: continue

        action = command[0]
        if action == 'quit': break
        if action == 'search': enter_search_console()

        continue
    return


def enter_search_console():
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
    while not category_name in utility.get_categories():
        print(f"'{category_name}' not found.")
        print("Choose an existing category or create 'new':")
        output.print_categories()
        new_category_name = input("category or 'new'> ")
        if new_category_name == 'new': 
            category.create_category(category_name)
            category_name = new_category_name
            break 
    return category_name


def confirm_notepack_console(category_name, notepack):
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


def pick_from_list(items, prompt="notepack> "):
    while True:
        requested_item = input(prompt)
        if requested_item in items:
            break
        else:
            print(f"'{requested_item}' is not available.")
            print(f"Try one of these: {items}")

    return requested_item


