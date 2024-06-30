import os

from . import data


def store_dir(directory="."):
    """Store the given directory in .gitd"""
    # List for entries
    entries = []
    # Scan the given directory
    with os.scandir(directory) as curr_dir:
        # Check every entry in current directory
        for entry in curr_dir:
            # Save entry's full path
            full_path = f"{directory}/{entry.name}"

            # If the path is ignored, continue to the next entry
            if ignore_dir(full_path):
                continue

            # If it is a file, write it hashed to the object dir
            if entry.is_file(follow_symlinks=False):
                entry_type = "file"
                with open(full_path, "rb") as file:
                    object_id = data.hash_file(file.read())

            # If it's a directory, scan it further
            elif entry.is_dir(follow_symlinks=False):
                entry_type = "dir"
                object_id = store_dir(full_path)

            # Store the entry
            entries.append((entry.name, object_id, entry_type))

    dir = "".join(f"{entry_type} {object_id} {name}\n"
                  for name, object_id, entry_type in sorted(entries))
    return data.hash_file(dir.encode(), "dir")


def ignore_dir(path):
    """Ignore returned directory"""
    return ".gitd" in path.split("/")
