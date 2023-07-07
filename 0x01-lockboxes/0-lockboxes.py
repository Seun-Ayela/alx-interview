#!/usr/bin/python3

def canUnlockAll(boxes):
    total_boxes = len(boxes)
    unlocked_boxes = [False] * total_boxes
    unlocked_boxes[0] = True

    # Iterate through the keys and unlock the corresponding boxes
    keys = boxes[0]
    for key in keys:
        if key < total_boxes:
            unlocked_boxes[key] = True

    # Iterate through the unlocked boxes and check if their keys can unlock more boxes
    for i in range(total_boxes):
        if unlocked_boxes[i]:
            keys = boxes[i]
            for key in keys:
                if key < total_boxes:
                    unlocked_boxes[key] = True

    # Check if all boxes are unlocked
    return all(unlocked_boxes)
