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

        category = confirm_category_console(command[0])
        notepack = confirm_notepack_console(category, command[1])

        print(f"Opening {notepack} in {category}")
    return


def confirm_category_console(category):
    while not category in utility.get_categories():
        print(f"'{category}' not found.")
        print("Choose an existing category or create 'new':")
        output.print_categories()
        new_category = input("category or 'new'> ")
        if new_category == 'new': break # Create the category.
    return category


def confirm_notepack_console(category, notepack):
    while not notepack in utility.get_notepacks(category):
        print(f"'{notepack}' NOT found!")
        print("Choose an existing notepack or creaste 'new':")
        output.print_notepacks(category)
        new_notepack = input("notepack or 'new'> ")
        if new_notepack == 'new': break # Create the notepack.
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


