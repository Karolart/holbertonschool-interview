#!/usr/bin/python3
""" defines method to solve lockboxes  """


def canUnlockAll(boxes):
    """
    Description:
    Write a method that determines if all the boxes can be opened
    Arguments:
    boxes --> List of Lists, it contains the boxes with keys
    Reurn boolean
    """
    unlocked = [0]
    for box_key, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked and key != box_key:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
