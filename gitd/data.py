import os
import hashlib


# gitd directory
GITD_DIR = ".gitd"


def init():
    """Initialize gitd directory"""
    # Create .gitd
    os.makedirs(GITD_DIR)
    # Make objects directory
    os.makedirs(f"{GITD_DIR}/objects")


def hash_file(data, entry_type="file"):
    """Hash given data using SHA-1 algorithm, store it in object directory of .gitd"""
    data_object = entry_type.encode() + b"\x00" + data
    # Hash the data
    file_id = hashlib.sha1(data).hexdigest()
    # Create a new hashed file, write to it
    with open(f"{GITD_DIR}/objects/{file_id}", "wb") as out:
        out.write(data_object)

    # Return hashed data
    return file_id


def get_file(file_id):
    """Get file by hashed id"""
    with open(f"{GITD_DIR}/objects/{file_id}", "rb") as file:
        return file.read()
