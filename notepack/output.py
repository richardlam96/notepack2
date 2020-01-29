"""
Output functions

Functions to aid in outputting messages to the console in specified format.
"""
from datetime import datetime


def show_welcome_message():
    """Print a welcome message to the output."""
    now = datetime.now()

    # Welcome message (this can be ASCII-art later).
    print("Welcome to Notepack App 2.0")
    print(f"It's {now}")


