
from model.tree_node import TreeNode
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative approach using stack

        Time: O(n) - visit each node once
        Space: O(h) - stack height equals tree height
        """
        # Edge case: empty tree
        if not root:
            return []

        result = []
        stack = []
        current = root

        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process node
            current = stack.pop()
            result.append(current.val)

            # Move to right subtree
            current = current.right

        return result

    def inorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursive approach

        Time: O(n)
        Space: O(h) - recursion stack
        """
        result = []

        def traverse(node):
            if not node:
                return

            # Inorder: Left -> Root -> Right
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)
        return result


def main():
    solution = Solution()

    # Test case 1: [1,null,2,3]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    assert solution.inorderTraversal(root1) == [1, 3, 2]
    assert solution.inorderTraversalRecursive(root1) == [1, 3, 2]

    # Test case 2: empty tree
    assert solution.inorderTraversal(None) == []
    assert solution.inorderTraversalRecursive(None) == []

    # Test case 3: single node
    root3 = TreeNode(1)
    assert solution.inorderTraversal(root3) == [1]
    assert solution.inorderTraversalRecursive(root3) == [1]

    # Test case 4: complete tree [1,2,3,4,5,6,7]
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    assert solution.inorderTraversal(root4) == [4, 2, 5, 1, 6, 3, 7]
    assert solution.inorderTraversalRecursive(root4) == [4, 2, 5, 1, 6, 3, 7]

    # Test case 5: left-skewed tree
    root5 = TreeNode(3)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(1)
    assert solution.inorderTraversal(root5) == [1, 2, 3]
    assert solution.inorderTraversalRecursive(root5) == [1, 2, 3]

    print("All tests passed!")


if __name__ == "__main__":
    main()
