from typing import Optional

class Node:
    def __init__(self, data):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.data: int = data

def insert(root: Optional[Node], data: int) -> Optional[Node]:
    if root is None:
        return Node(data) # type: ignore
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root


def height(root: Optional[Node]) -> int:
    if root is None:
        return -1
    else:
        left_height = height(root.left)
        reight_height = height(root.right)

        return 1 + max(left_height, reight_height)