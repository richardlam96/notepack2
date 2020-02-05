"""
Actions for the category entity: Create, List, Use, Delete.

NOTE: These are probably going to be very similar to notepack actions since
later, the idea is that categories will also be notepacks, just parent
notepacks and the testflows there will be considered "Feature Testflows".
"""
from pathlib import Path
from notepack import config
from notepack import utility


category_actions = {
    "create": create_category,
    "list": list_categories,
    "use": use_category,
    "delete": delete_category,
}


def create_category(category):
    print("Category")
    category_path = Path(utility.get_category_path(category))
    try:
        print(f"  Creating {category}...")
        category_path.mkdir()
        print(f"  {category} created!")
    except FileExistsError:
        print(f"  {category} already exists.")
    return


def list_categories():
    """List categories in the path from config."""
    categories = utility.get_path_items(config.DEFAULT_FOLDERS['tickets'])
    if len(categories) == 0:
        print("No categories to show")
    else:
        print('\n'.join(categories))
    return


def use_category(category):
    """Validate that category exists."""
    while True:
        category_path = utility.get_category_path(category)
        if not category_path.exists():
            print(f"The category '{category}' does not exist. Choose another:")
            list_categories()
            category = input('> ')
        else: break
    return category


def delete_category(category):
    """Delete category, but validate if all contents should be removed."""
    return
