
from model import TreeNode


def arrayToBST(arr):
    """
    Helper function to create a BST from a sorted array.
    """
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = arrayToBST(arr[:mid])
    root.right = arrayToBST(arr[mid + 1:])
    return root
