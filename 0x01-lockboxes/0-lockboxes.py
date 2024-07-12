#!/usr/bin/python3
"""method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False """
    if not boxes or type(boxes) is not list:
        return False

    opened = [0]
    for element in opened:
        for box in boxes[element]:
            if box not in opened and box < len(boxes):
                opened.append(box)
    if len(opened) == len(boxes):
        return True
    return False
