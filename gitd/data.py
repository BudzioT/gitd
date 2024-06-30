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


def hash_object(data):
    """Hash given data using SHA-1 algorithm, store it in object directory of .gitd"""
    # Hash the data
    object_id = hashlib.sha1(data).hexdigest()
    # Create a new hashed file, write to it
    with open(f"{GITD_DIR}/objects/{object_id}", "wb") as out:
        out.write(data)

    # Return hashed data
    return object_id
