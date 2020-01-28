"""
Output functions

Functions to aid in outputting messages to the console in specified format.
"""
from datetime import date


def show_welcome_message():
    """Print a welcome message to the output."""
    today = date.today()

    # Welcome message (this can be ASCII-art later).
    print("Welcome to Notepack App 2.0")
    print(f"It's {today}.")


