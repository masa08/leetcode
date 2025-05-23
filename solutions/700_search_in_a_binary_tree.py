from typing import Optional
from model import TreeNode
from utils import makeBinarySearchTree


def main():
    # Create test data: Binary Search Tree (BST)
    # Example tree:
    #        4
    #       / \
    #      2   7
    #     / \
    #    1   3
    args = [1, 2, 3, 4, 7]  # Sorted array to create a BST
    root = makeBinarySearchTree(args)

    # Value to search
    val = 2

    # Apply the solution
    solution = Solution()
    result = solution.searchBST(root, val)

    # Print the result
    if result:
        print(f"Node found with value: {result.val}")
    else:
        print("Value not found in the BST.")


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def _searchBST(root, val):
            if root is None:
                return None
            if root.val == val:
                return root

            if val < root.val:
                return _searchBST(root.left, val)
            else:
                return _searchBST(root.right, val)

        return _searchBST(root, val)


if __name__ == '__main__':
    main()
