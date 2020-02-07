"""
Entry point for the Notepack app.

"""
from notepack import output
from notepack import utility
from notepack import initialize
from notepack.actions import category


def notepack():
    """Begin the app with the main console

    Includes printing messages and checking for required folders and files.
    """
    output.print_welcome_message()
    initialize.confirm_required_folders()
    initialize.confirm_required_files()

    # Start the main notepack console.
    print("What would you like to do?")
    while True:
        command = input("> ").split()
        if not command: continue

        action = command[0]
        if action == 'quit': break
        if action == 'search': enter_search_console()

        continue
    return


def enter_search_console():
    """Search console
    
    One type of console used to search and open a notepack.
    """
    print("Search Console")
    while True:
        command = input("search> ").split()
        if not command: continue
        if command[0] == 'quit': break
        
        # Breakdown of command (for clarity).
        category_name = command[0]
        notepack_name = command[1]
        category_path = utility.get_root_path().joinpath(category_name)
        notepack_path = category_path.joinpath(notepack_name)

        # Confirm if you need to create the category and notepack paths.
        category_path = confirm_path_console(category_path)
        notepack_path = confirm_path_console(notepack_path)

        # Create any missing files and paths for the notepack.

    return


def confirm_path_console(requested_path):
    """General sub-console for searching and creating entities"""
    while not requested_path.exists():
        # List items in the parent folder to re-choose child.
        print(f"'{requested_path.name}' does not exist.")
        print("Choose existing or create 'new':")
        '\n'.join(utility.get_path_items(requested_path.parent))
        new_path_name = input("existing or 'new'> ")

        if new_path_name == 'new':
            return utility.create_path(requested_path)
        elif new_path_name == 'quit':
            break
        else:
            requested_path = requested_path.parent.joinpath(new_path_name)

    return


def pick_from_list(items, prompt="> "):
    while True:
        requested_item = input(prompt)
        if requested_item in items:
            break
        else:
            print(f"'{requested_item}' is not available.")
            print(f"Try one of these: {items}")

    return requested_item


