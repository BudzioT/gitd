import argparse
import os
import sys

from . import data
from . import baseLogic


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

    # Add hash_file command
    hash_parser = commands.add_parser("hash_file")
    # Synchronize it with hash_object function
    hash_parser.set_defaults(func=hash_file)
    # Add a file argument
    hash_parser.add_argument("file")

    # Add write_dir command
    write_dir_parser = commands.add_parser("write_dir")
    write_dir_parser.set_defaults(func=write_dir)
    write_dir_parser.add_argument("--dir", default=".")

    # Add print_file
    print_file_parser = commands.add_parser("print_file")
    print_file_parser.set_defaults(func=print_file)
    print_file_parser.add_argument("file")

    # Return parser arguments
    return parser.parse_args()


def init(args):
    """Initialize repository"""
    # Create the repository
    data.init()
    # Inform the user about the location of it
    print(f"Initialized an empty gitd repo at location: {os.getcwd()}/{data.GITD_DIR}")


def hash_file(args):
    """Hash given file using SHA-1 algorithm, store it in object directory of .gitd"""
    # Hash the file, open it and print the saved data
    with open(args.file, "rb") as file:
        data.hash_file(file.read())
    print(f"Successfully hashed {args.file} into repo directory")


def write_dir(args):
    """Write a directory to the gitd"""
    baseLogic.store_dir(args.dir)
    print(baseLogic.store_dir())


def print_file(args):
    """Print hashed file after rehashing it"""
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_file(args.file))
