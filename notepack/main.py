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

    actions = ["create", "open", "delete"]

    # Start of the notepack "terminal".
    print("What would you like to do?")
    while True:
        command = input("> ").split()
        action = command[0]
        entity = command[1]
        if not command: continue
        if action == 'quit': break

        # Validate availability of action and entity.
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


