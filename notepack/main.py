"""
Entry point for the Notepack app.

"""
from notepack import output
from notepack import utility
from notepack import initialize
from notepack.actions import actions


def notepack():
    output.show_welcome_message()
    initialize.confirm_required_folders()
    initialize.confirm_required_files()

    actions = ["create", "open", "delete"]

    # Start of the notepack "terminal".
    print("What would you like to do?")
    while True:
        command = input("> ").split()
        # Process commands.
        if command[0] == 'quit':
            break
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


