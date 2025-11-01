from model import TreeNode
from typing import Optional


def main():
    solution = Solution()

    # Test case 1: Valid BST
    #     2
    #    / \
    #   1   3
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    result = solution.isValidBST(root1)
    assert result == True, f"Expected True, got {result}"
    print(f"Test 1 (Valid BST): {result}")

    # Test case 2: Invalid BST
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    result = solution.isValidBST(root2)
    assert result == False, f"Expected False, got {result}"
    print(f"Test 2 (Invalid BST): {result}")

    # Test case 3: Edge case - single node
    root3 = TreeNode(1)
    result = solution.isValidBST(root3)
    assert result == True, f"Expected True, got {result}"
    print(f"Test 3 (Single node): {result}")

    # Test case 4: Edge case - invalid with duplicate
    #     2
    #    / \
    #   2   2
    root4 = TreeNode(2)
    root4.left = TreeNode(2)
    root4.right = TreeNode(2)
    result = solution.isValidBST(root4)
    assert result == False, f"Expected False, got {result}"
    print(f"Test 4 (Duplicates): {result}")

    # Test case 5: Tricky case - values exceed parent bounds
    #      10
    #     /  \
    #    5   15
    #       /  \
    #      6   20
    root5 = TreeNode(10)
    root5.left = TreeNode(5)
    root5.right = TreeNode(15)
    root5.right.left = TreeNode(6)
    root5.right.right = TreeNode(20)
    result = solution.isValidBST(root5)
    assert result == False, f"Expected False, got {result}"
    print(f"Test 5 (Violates ancestor bounds): {result}")

    print("All tests passed!")


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validate BST by checking each node's value range.

        Each node must satisfy: min_value < node.val < max_value

        Time: O(n) - visit each node once
        Space: O(h) - recursion stack
        """
        return self._isValid(root, min_value=float('-inf'), max_value=float('inf'))

    def _isValid(self, node: Optional[TreeNode], min_value: float, max_value: float) -> bool:
        # Empty tree is valid
        if not node:
            return True

        # Current node must be within valid range
        if not (min_value < node.val < max_value):
            return False

        # Left subtree: all values must be less than current node
        # Right subtree: all values must be greater than current node
        is_left_valid = self._isValid(node.left, min_value, node.val)
        is_right_valid = self._isValid(node.right, node.val, max_value)

        return is_left_valid and is_right_valid


if __name__ == '__main__':
    main()
