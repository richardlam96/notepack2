"""
Output functions

Functions to aid in outputting messages to the console in specified format.
Console logger with datetime and spacing.
"""
from datetime import datetime


def print_welcome_message():
    """Print a welcome message to the output."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Welcome message (this can be ASCII-art later).
    print("Welcome to Notepack App 2.0")
    print(f"It's {now}")


