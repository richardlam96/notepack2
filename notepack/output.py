"""
Output functions

Functions to aid in outputting messages to the console in specified format.
"""
from datetime import datetime
from notepack import utility


def print_welcome_message():
    """Print a welcome message to the output."""
    now = datetime.now()

    # Welcome message (this can be ASCII-art later).
    print("Welcome to Notepack App 2.0")
    print(f"It's {now}")


def print_categories():
    categories = utility.get_categories()
    if len(categories) == 0:
        print("No categories to show")
    else:
        print('\n'.join(categories))
    return


def print_notepacks(category):
    categories = utility.get_notepacks(category)
    if len(categories) == 0:
        print("No categories to show")
    else:
        print('\n'.join(categories))
    return

