"""
Entry point for the Notepack app.

"""
from . import initialize
from . import output


def notepack():
    output.show_welcome_message()
    initialize.initialize_app()


