#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Method that determines if all the boxes can be opened """
    if not boxes:
        return False
    if len(boxes) == 1:
        return True
    keys = [0]
    for key in keys:
        for newKey in boxes[key]:
            if newKey not in keys and newKey < len(boxes):
                keys.append(newKey)
    if len(keys) == len(boxes):
        return True
    return False
