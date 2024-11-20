import os
from hashlib import sha1


def verify():
    assert os.path.exists("solution.txt"), "FAIL: solution.txt does not exist"

    with open("solution.txt") as file:
        solution = sha1(file.read().strip().lower().encode("utf-8")).hexdigest()

    assert (
        solution == "0eb5e7cbfd8eb32c61f4f3b359e1988e876396af"), "FAIL: incorrect solution"

    print("SUCCESS: challenge completed.")
    return True


verify()
