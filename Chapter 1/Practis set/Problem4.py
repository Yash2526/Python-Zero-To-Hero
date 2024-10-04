# Que.4

# Write a python program to print the content of a directory using the os modual.
# serch Online for the function which does that.

import os

def list_directory_contents(path='/'):
    try:
        # Get the list of all files and directories
        directory_contents = os.listdir(path)
        print(f"Contents of the directory '{path}':")
        for item in directory_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing the directory '{path}'.")

# Example usage
list_directory_contents('/')  # Lists the contents of the current directory
