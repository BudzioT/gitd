import argparse
import os
from . import data


def main():
    """Main function - the gitd"""
    # Get arguments
    args = parse_args()
    # Use functions set by arguments
    args.func(args)


def parse_args():
    """Setup argument parser"""
    # Create an argument parser
    parser = argparse.ArgumentParser()

    # Create a subparser, require it (used for subcommands like init...)
    commands = parser.add_subparsers(dest="command")
    commands.required = True

    # Add init command, use init function when called
    init_parser = commands.add_parser("init")
    init_parser.set_defaults(func=init)

    # Add hash command
    hash_object_parser = commands.add_parser("hash")
    # Synchronize it with hash_object function
    hash_object_parser.set_defaults(func=hash_object)
    # Add a file argument
    hash_object_parser.add_argument("file")

    # Return parser arguments
    return parser.parse_args()


def init(args):
    """Initialize repository"""
    # Create the repository
    data.init()
    # Inform the user about the location of it
    print(f"Initialized an empty gitd repo at location: {os.getcwd()}/{data.GITD_DIR}")


def hash_object(args):
    """Hash given file using SHA-1 algorithm, store it in object directory of .gitd"""
    # Hash the file, open it and print the saved data
    with open(args.file, "rb") as file:
        print(data.hash_object(file.read()))
