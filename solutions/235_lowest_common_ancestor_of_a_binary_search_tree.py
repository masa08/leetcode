from typing import Optional

from model import TreeNode
from utils import makeTree


def main():
    solution = Solution()

    # Basic cases
    root1 = makeTree([6, 2, 8, 1, 4, 7, 9])
    assert solution.lowestCommonAncestor(
        root1, find_node(root1, 2), find_node(root1, 8)).val == 6
    assert solution.lowestCommonAncestor(
        root1, find_node(root1, 2), find_node(root1, 4)).val == 2

    # Edge cases
    root2 = makeTree([2, 1])
    assert solution.lowestCommonAncestor(
        root2, find_node(root2, 2), find_node(root2, 1)).val == 2

    print("All tests passed!")


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Algorithm: Split point search using BST property

        BST Property: left subtree < root < right subtree

        Strategy:
        1. If both p and q are smaller than current node → move to left subtree
        2. If both p and q are greater than current node → move to right subtree
        3. Otherwise (one on left, one on right, or one is current) → split point = LCA

        Complexity:
        - Time: O(h) where h is height of tree
          - Balanced BST: O(log n)
          - Skewed BST: O(n)
          - At most one traversal from root to leaf
        - Space: O(1)
          - Iterative approach requires no additional memory
          - Recursive version would require O(h) stack space

        Note: Unlike regular binary tree (problem 236), we can determine LCA by value comparison only
        """
        while root:
            # Both nodes in left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # Both nodes in right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # Split point found - this is the LCA
            else:
                return root


def find_node(root: TreeNode, val: int) -> Optional[TreeNode]:
    """Helper to find node with given value"""
    if not root:
        return None
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.val == val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None


if __name__ == "__main__":
    main()
