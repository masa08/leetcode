from model.tree_node import TreeNode
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative approach using stack

        Time: O(n) - visit each node once
        Space: O(h) - stack height equals tree height
        """
        # Edge case: empty tree
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            # Process root
            node = stack.pop()
            result.append(node.val)

            # Push right first (so left is processed first)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

    def preorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursive approach

        Time: O(n)
        Space: O(h) - recursion stack
        """
        result = []

        def traverse(node):
            if not node:
                return

            # Preorder: Root -> Left -> Right
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return result


def main():
    solution = Solution()

    # Test case 1: [1,null,2,3]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    assert solution.preorderTraversal(root1) == [1, 2, 3]
    assert solution.preorderTraversalRecursive(root1) == [1, 2, 3]

    # Test case 2: empty tree
    assert solution.preorderTraversal(None) == []
    assert solution.preorderTraversalRecursive(None) == []

    # Test case 3: single node
    root3 = TreeNode(1)
    assert solution.preorderTraversal(root3) == [1]
    assert solution.preorderTraversalRecursive(root3) == [1]

    # Test case 4: complete tree [1,2,3,4,5,6,7]
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    assert solution.preorderTraversal(root4) == [1, 2, 4, 5, 3, 6, 7]
    assert solution.preorderTraversalRecursive(root4) == [1, 2, 4, 5, 3, 6, 7]

    print("All tests passed!")


if __name__ == "__main__":
    main()
