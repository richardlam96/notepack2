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

        category = command[0]
        if category == 'quit': break

        notepack = command[1]

        if category in utility.get_categories():
            print(f"'{category}' found!")
        else:
            print(f"'{category}' NOT found!")


    return


def pick_from_list(items, prompt="notepack> "):
    while True:
        requested_item = input(prompt)
        if requested_item in items:
            break
        else:
            print(f"'{requested_item}' is not available.")
            print(f"Try one of these: {items}")

    return requested_item


