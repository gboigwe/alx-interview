#!/usr/bin/python3
"""Unlocking key to list of list that matches boxes"""


def canUnlockAll(boxes):
    """Unlocking of all boxes if possible"""

    if (type(boxes) is not list or len(boxes) == 0):
        return False

    lenBox = len(boxes)
    for key in range(1, lenBox - 1):
        unlockBox = False
        for i in range(lenBox):
            unlockBox = key in boxes[i] and key != i
            if unlockBox:
                break
        if unlockBox is False:
            return unlockBox
    return True
