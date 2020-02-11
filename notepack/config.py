"""
Configuration for the notepack app.

This includes all the folders and files that are expected for the app to work.
Directories would basically be references to entities.
Files would be references to templates.
"""
DEFAULT_FOLDERS = {
    "tickets": "./tickets", 
    "templates": "./templates",
}

DEFAULT_TEMPLATES = {
    "description.md": DEFAULT_FOLDERS['templates'] + "/description.md",
    "testflow.md": DEFAULT_FOLDERS['templates'] + "/testflow.md",
    "testing_story.md": DEFAULT_FOLDERS['templates'] + "/testing_story.md",
    "testing_summary.md": DEFAULT_FOLDERS['templates'] + "/testing_summary.md",
}

CATEGORY_CONFIG = {
    "directories":  [],
    "files": ["description.md"]
}

NOTEPACK_CONFIG = {
    "directories": ['picture', 'script', 'testflow'],
    "files": ["description.md", "testing_story.md", "testing_summary.md"]
}

TESTFLOW_CONFIG = {
    "directories": [],
    "files": ["testflow.md"],
}

ENTITIES = {
    "category": CATEGORY_CONFIG, 
    "notepack": NOTEPACK_CONFIG,
    "testflow": TESTFLOW_CONFIG
}


