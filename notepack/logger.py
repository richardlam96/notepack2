"""
Functions to help print output in a more organized fashion.
"""
from datetime import datetime


def print_welcome_message():
    print("Welcome to Notepack App 2.0")


def log(message, depth=0, character='.'):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    spacing = character * depth * 2
    print(f"[{time_now}] {spacing}{message}")
    return


def prompt(prompt, depth=0, character='.'):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    spacing = character * depth * 2
    return input(f"[{time_now}] {spacing}{prompt}> ")
