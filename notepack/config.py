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

ENTITIES = ['category', 'testflows']

CATEGORY_CONFIG = {
    "directores":  [],
    "files": "description.md"
}

NOTEPACK_CONFIG = {
    "directories": ['pictures', 'scripts', 'testflows'],
    "files": ["description.md", "testing_story.md", "test_summary.md"]
}

TESTFLOW_CONFIG = {
    "directories": [],
    "files": ["testflow_mk0.md"],
}
