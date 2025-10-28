from model import TreeNode
from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Check if subRoot is a subtree of root.

        Approach: DFS + Tree Comparison
        - Traverse the main tree (root)
        - At each node, check if the tree rooted at that node is identical to subRoot
        - Use helper function isSameTree (from problem 100)

        Time Complexity: O(m * n) where m is nodes in root, n is nodes in subRoot
        Space Complexity: O(h) where h is the height of root (recursion stack)
        """
        # Empty subRoot is always a subtree
        if not subRoot:
            return True

        # Empty root cannot contain non-empty subRoot
        if not root:
            return False

        # Check if trees are the same starting from current node
        if self.isSameTree(root, subRoot):
            return True

        # Recursively check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Helper function to check if two trees are identical.
        (Same as Problem 100: Same Tree)
        """
        # Both trees are empty
        if not p and not q:
            return True

        # One tree is empty, the other is not
        if not p or not q:
            return False

        # Both nodes exist - check value and recurse on subtrees
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def main():
    solution = Solution()

    # Test case 1: subRoot is a subtree
    #     3
    #    / \
    #   4   5
    #  / \
    # 1   2
    # subRoot: 4
    #         / \
    #        1   2
    root1 = TreeNode(3)
    root1.left = TreeNode(4)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(2)

    subRoot1 = TreeNode(4)
    subRoot1.left = TreeNode(1)
    subRoot1.right = TreeNode(2)

    assert solution.isSubtree(root1, subRoot1) == True, "Test case 1 failed"

    # Test case 2: subRoot is NOT a subtree (has extra node)
    #     3
    #    / \
    #   4   5
    #  / \
    # 1   2
    #    /
    #   0
    # subRoot: 4
    #         / \
    #        1   2
    root2 = TreeNode(3)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(0)

    subRoot2 = TreeNode(4)
    subRoot2.left = TreeNode(1)
    subRoot2.right = TreeNode(2)

    assert solution.isSubtree(root2, subRoot2) == False, "Test case 2 failed"

    # Test case 3: Single node - match
    root3 = TreeNode(1)
    subRoot3 = TreeNode(1)
    assert solution.isSubtree(root3, subRoot3) == True, "Test case 3 failed"

    # Test case 4: Single node - no match
    root4 = TreeNode(1)
    subRoot4 = TreeNode(2)
    assert solution.isSubtree(root4, subRoot4) == False, "Test case 4 failed"

    # Test case 5: Empty subRoot
    root5 = TreeNode(1)
    assert solution.isSubtree(root5, None) == True, "Test case 5 failed"

    # Test case 6: Empty root with non-empty subRoot
    subRoot6 = TreeNode(1)
    assert solution.isSubtree(None, subRoot6) == False, "Test case 6 failed"

    # Test case 7: Subtree at right side
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    # subRoot: 3
    #         / \
    #        4   5
    root7 = TreeNode(1)
    root7.left = TreeNode(2)
    root7.right = TreeNode(3)
    root7.right.left = TreeNode(4)
    root7.right.right = TreeNode(5)

    subRoot7 = TreeNode(3)
    subRoot7.left = TreeNode(4)
    subRoot7.right = TreeNode(5)

    assert solution.isSubtree(root7, subRoot7) == True, "Test case 7 failed"

    # Test case 8: Values match but structure doesn't
    #     1
    #    /
    #   1
    # subRoot: 1
    root8 = TreeNode(1)
    root8.left = TreeNode(1)
    subRoot8 = TreeNode(1)
    assert solution.isSubtree(root8, subRoot8) == True, "Test case 8 failed"

    print("All tests passed!")


if __name__ == "__main__":
    main()
