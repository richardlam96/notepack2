"""
Entry point for the Notepack app.

"""
import shutil
from pathlib import Path
from notepack import initialize
from notepack import logger
from notepack import config
from notepack import config_util


def notepack():
    """Begin the app with the main console

    Includes printing messages and checking for required folders and files.
    """
    try:
        logger.print_welcome_message()
        initialize.confirm_required_folders()
        initialize.confirm_required_files()

        # Start the main notepack console.
        while True:
            command = logger.prompt("What would you like to do?").split()
            if not command: continue

            action = command[0]
            if action == 'quit': break
            if action == 'search': enter_search_console()

            continue
    except KeyboardInterrupt:
        logger.output("Forced exit with keyboard interrupt.")


def enter_search_console():
    """Search console
    
    One type of console used to search and open a notepack.
    """
    logger.output("SEARCH MODE")
    while True:
        command = logger.prompt("search").split()
        if not command: continue
        if command[0] == 'quit': break
        
        # Breakdown of command (for clarity).
        try:
            category_name = command[0]
            notepack_name = command[1]
        except IndexError:
            logger.output(f"Improper input. Try again.")
            continue

        # Create the Path objects for each.
        root_path = Path(config_util.read_root_path())
        category_path = root_path.joinpath(category_name)
        notepack_path = category_path.joinpath(notepack_name)

        # Confirm if Paths are new and need to be created.
        category_path = confirm_path_console(category_path)
        notepack_path = confirm_path_console(notepack_path)

        # Create any missing files and paths for the notepack.
        confirm_files_and_directories(category_path, 'category')
        confirm_files_and_directories(notepack_path, 'notepack')


def confirm_path_console(requested_path):
    """
    General sub-console for searching and creating entities

    Used for validating paths, returning one that definitely exists.
    """
    while not requested_path.exists():
        # List items in the parent folder to re-choose child.
        logger.output(f"'{requested_path}' does not exist.")
        logger.output("Choose existing or create 'new':")
        logger.output('\n'.join(get_path_items(requested_path.parent)))
        new_path_name = logger.prompt("existing or 'new'")

        if new_path_name == 'new':
            requested_path.mkdir()
            break
        elif new_path_name == 'quit':
            break
        else:
            requested_path = requested_path.parent.joinpath(new_path_name)

    return requested_path


def confirm_files_and_directories(entity_path, entity_name):
    """
    For any entities with existing configs, recursively create missing
    files.
    """
    for directory in config_util.read_dir_names(entity_name):
        directory_path = entity_path.joinpath(directory)
        if directory_path.exists():
            logger.output(f"{directory} exists in {entity_path}")
        else:
            logger.output(f"Creating {directory} in {entity_path}")
            directory_path.mkdir()

        # If directory is also a listed entity, recursively call this function.
        if directory in config.ENTITIES.keys():
            confirm_files_and_directories(directory_path, directory)

    for template_file in config_util.read_file_names(entity_name):
        template_file_path = entity_path.joinpath(template_file)
        if template_file_path.exists():
            logger.output(f"{template_file} exists in {entity_path}")
        else:
            logger.output(f"Creating {template_file} in {entity_path}")
            shutil.copy(config_util.read_template_path(template_file), entity_path)
    return


def get_path_items(path):
    """Get items in a given path in an array."""
    posix_path = Path(path)
    return [path.name for path in posix_path.glob('*')]



