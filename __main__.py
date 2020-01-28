# Notepack 2
#
# Version 2 of the Notepack, which will primarily use Pythopn as the main
# language instead of bash to allow more functionality for future enhancements.
#
from datetime import date
import os

def main():
    today = date.today()

    # Welcome message (this can be ASCII-art later).
    print("Welcome to Notepack App 2.0")
    print(f"It's {today}.")

    # Check if tickets/ exists. TODO: Generalize to all required files.
    if not os.path.exists("./tickets"):
        print("Initial files and folders not found.")
        action = input("Create? (Y/n): ")
        if action == 'n':
            print("WARNING: tickets/ path was not created!")
        os.mkdir("./tickets")
        print("tickets/ folder made")

    # List directories.
    print(os.listdir('./tickets'))
    

if __name__ == "__main__":
    main()
