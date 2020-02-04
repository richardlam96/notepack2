"""
Entry point for the Notepack app.

"""
from notepack import output
from notepack import actions
from notepack import utility
from notepack.initialize import initialize_app


def notepack():
    output.show_welcome_message()
    initialize_app()  # Not the most necessary. Add as action.

    actions = ["create", "open", "delete"]

    print("What would you like to do?")
    command = input("> ").split()
    action = confirm_choice(command[0], actions)
    category = confirm_choice(command[1], utility.list_categories())
    notepack = confirm_choice(command[2], utility.list_notepacks())
    return


def confirm_choice(choice, choice_list):
    if choice not in choice_list:
        choice = pick_from_list(choice_list)
    return choice


def pick_from_list(items, prompt="notepack> "):
    while True:
        requested_item = input(prompt)
        if requested_item in items:
            break
        else:
            print(f"'{requested_item}' is not available.")
            print(f"Try one of these: {items}")

    return requested_item


