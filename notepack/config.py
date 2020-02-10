"""
Configuration for the notepack app.

This includes all the folders and files that are expected for the app to work.
"""
DEFAULT_FOLDERS = {
    "tickets": "./tickets", 
    "templates": "./templates",
}

DEFAULT_TEMPLATES = {
    "description": DEFAULT_FOLDERS['templates'] + "/description.md",
    "testflow": DEFAULT_FOLDERS['templates'] + "/testflow.md",
    "testing_story": DEFAULT_FOLDERS['templates'] + "/testing_story.md",
    "testing_summary": DEFAULT_FOLDERS['templates'] + "/testing_summary.md",
}

CATEGORY_CONFIG = {
    "directories":  [],
    "files": ["description"]
}

NOTEPACK_CONFIG = {
    "directories": ['pictures', 'scripts', 'testflows'],
    "files": ["description", "testing_story", "testing_summary"]
}

TESTFLOW_CONFIG = {
    "directories": [],
    "files": ["testflow"],
}

ENTITIES = {
    "category": CATEGORY_CONFIG, 
    "notepack": NOTEPACK_CONFIG,
    "testflows": TESTFLOW_CONFIG
}


