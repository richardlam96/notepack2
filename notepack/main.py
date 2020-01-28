"""
Entry point for the Notepack app.

"""
from notepack.initialize import initialize_app
from notepack.output import show_welcome_message


def notepack():
    show_welcome_message()
    initialize_app()


