from typing import Optional

from model import TreeNode


def main():
    # Create test data: Binary tree
    # Example tree:
    #        3
    #       / \
    #      9   20
    #         /  \
    #        15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Apply the solution
    solution = Solution()
    result = solution.sumOfLeftLeaves(root)

    # Print the result
    print(f"Sum of left leaves: {result}")


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def _sumOfLeftLeaves(self, root, isLeft) -> int:
            if root and not root.right and not root.left:
                return root.val if isLeft else 0

            total = 0
            if root.left:
                total += _sumOfLeftLeaves(self, root.left, True)
            if root.right:
                total += _sumOfLeftLeaves(self, root.right, False)
            return total

        return _sumOfLeftLeaves(self, root, False)


if __name__ == '__main__':
    main()
