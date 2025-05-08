
from model import TreeNode


def makeBinarySearchTree(arr):
    """
    Helper function to create a BST from a sorted array.
    """
    if not arr:
        return None

    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = makeBinarySearchTree(arr[:mid])
    root.right = makeBinarySearchTree(arr[mid + 1:])
    return root
