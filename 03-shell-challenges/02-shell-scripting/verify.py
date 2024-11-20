import os
from hashlib import sha1


def verify():
    assert os.path.exists("solution.txt"), "FAIL: solution.txt does not exist"

    with open("solution.txt") as file:
        solution = sha1(file.read().strip().lower().encode("utf-8")).hexdigest()

    assert (
        solution == "3c6336c16d7ab4cd66037b750362667925b73339"
    ), "FAIL: incorrect solution"

    print("SUCCESS: challenge completed.")
    return True


verify()
