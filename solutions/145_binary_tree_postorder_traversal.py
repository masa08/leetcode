from model.tree_node import TreeNode
from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative approach using two stacks

        Time: O(n) - visit each node once
        Space: O(h) - stack height equals tree height
        """
        # Edge case: empty tree
        if not root:
            return []

        result = []
        stack = [root]

        # Postorder is reverse of modified preorder (Root -> Right -> Left)
        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push left first (so right is processed first)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Reverse to get postorder (Left -> Right -> Root)
        return result[::-1]

    def postorderTraversalOneStack(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative approach using one stack with visited tracking

        Time: O(n)
        Space: O(h)
        """
        if not root:
            return []

        result = []
        stack = []
        current = root
        last_visited = None

        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Peek at the top node
            peek_node = stack[-1]

            # If right child exists and not visited, go right
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                # Process node
                stack.pop()
                result.append(peek_node.val)
                last_visited = peek_node

        return result

    def postorderTraversalRecursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursive approach

        Time: O(n)
        Space: O(h) - recursion stack
        """
        result = []

        def traverse(node):
            if not node:
                return

            # Postorder: Left -> Right -> Root
            traverse(node.left)
            traverse(node.right)
            result.append(node.val)

        traverse(root)
        return result


def main():
    solution = Solution()

    # Test case 1: [1,null,2,3]
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    assert solution.postorderTraversal(root1) == [3, 2, 1]
    assert solution.postorderTraversalOneStack(root1) == [3, 2, 1]
    assert solution.postorderTraversalRecursive(root1) == [3, 2, 1]

    # Test case 2: empty tree
    assert solution.postorderTraversal(None) == []
    assert solution.postorderTraversalOneStack(None) == []
    assert solution.postorderTraversalRecursive(None) == []

    # Test case 3: single node
    root3 = TreeNode(1)
    assert solution.postorderTraversal(root3) == [1]
    assert solution.postorderTraversalOneStack(root3) == [1]
    assert solution.postorderTraversalRecursive(root3) == [1]

    # Test case 4: complete tree [1,2,3,4,5,6,7]
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    assert solution.postorderTraversal(root4) == [4, 5, 2, 6, 7, 3, 1]
    assert solution.postorderTraversalOneStack(root4) == [4, 5, 2, 6, 7, 3, 1]
    assert solution.postorderTraversalRecursive(root4) == [4, 5, 2, 6, 7, 3, 1]

    # Test case 5: left-skewed tree
    root5 = TreeNode(3)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(1)
    assert solution.postorderTraversal(root5) == [1, 2, 3]
    assert solution.postorderTraversalOneStack(root5) == [1, 2, 3]
    assert solution.postorderTraversalRecursive(root5) == [1, 2, 3]

    print("All tests passed!")


if __name__ == "__main__":
    main()
