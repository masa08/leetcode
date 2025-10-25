from typing import Optional

from model import TreeNode
from utils import makeTree


def main():
    solution = Solution()

    # Basic cases
    assert solution.isBalanced(makeTree([3, 9, 20, None, None, 15, 7])) == True
    assert solution.isBalanced(
        makeTree([1, 2, 2, 3, 3, None, None, 4, 4])) == False

    # Edge cases
    assert solution.isBalanced(None) == True
    assert solution.isBalanced(makeTree([1])) == True
    assert solution.isBalanced(makeTree([1, 2])) == True

    print("All tests passed!")


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Check if binary tree is height-balanced.

        Definition of height-balanced:
        A binary tree is height-balanced if for every node in the tree,
        the absolute difference between the heights of its left and right
        subtrees is at most 1.
        """
        # Edge case: empty tree is balanced
        if not root:
            return True

        # DFS approach with helper function - PREFERRED
        # - Check height difference at each node
        # - Return UNBALANCED (-1) if unbalanced, height otherwise
        # - Time: O(n), Space: O(h) where h is height
        # - WHY?: Single pass through tree, early termination on unbalanced

        UNBALANCED = -1

        def checkHeightAndBalance(node: Optional[TreeNode]) -> int:
            """
            Returns:
                Height of subtree (>=0) if balanced
                UNBALANCED (-1) if any subtree is unbalanced
            """
            # Base case: null node has height 0
            if not node:
                return 0

            # Recursively check left subtree
            left_subtree_height = checkHeightAndBalance(node.left)
            if left_subtree_height == UNBALANCED:
                return UNBALANCED  # Early termination: left unbalanced

            # Recursively check right subtree
            right_subtree_height = checkHeightAndBalance(node.right)
            if right_subtree_height == UNBALANCED:
                return UNBALANCED  # Early termination: right unbalanced

            # Check if current node violates balance property
            height_difference = abs(left_subtree_height - right_subtree_height)
            if height_difference > 1:
                return UNBALANCED

            # Current node is balanced, return its height
            current_height = 1 + max(left_subtree_height, right_subtree_height)
            return current_height

        return checkHeightAndBalance(root) != UNBALANCED

        # Alternative: Naive approach (checking each node separately)
        # - Calculate height at each node and check difference
        # - Time: O(n^2) in worst case (recalculates heights)
        # - Space: O(h)
        # def height(node):
        #     if not node:
        #         return 0
        #     return 1 + max(height(node.left), height(node.right))
        #
        # if not root:
        #     return True
        #
        # left_height = height(root.left)
        # right_height = height(root.right)
        #
        # if abs(left_height - right_height) > 1:
        #     return False
        #
        # return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == '__main__':
    main()
