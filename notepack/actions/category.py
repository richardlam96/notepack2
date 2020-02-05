"""
CRUD actions for the category entity.

NOTE: These are probably going to be very similar to notepack actions since
later, the idea is that categories will also be notepacks, just parent
notepacks and the testflows there will be considered "Feature Testflows".
"""
from pathlib import Path


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


def show_categories():
    return


