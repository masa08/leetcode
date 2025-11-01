from model import TreeNode
from typing import Optional


def main():
    # Build test tree:
    #       3
    #      / \
    #     1   4
    #      \
    #       2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    solution = Solution()

    # Test case 1
    k = 1
    result = solution.kthSmallest(root, k)
    assert result == 1, f"Expected 1, got {result}"
    print(f"k={k}: {result}")

    # Test case 2
    k = 3
    result = solution.kthSmallest(root, k)
    assert result == 3, f"Expected 3, got {result}"
    print(f"k={k}: {result}")

    # Build test tree 2:
    #         5
    #        / \
    #       3   6
    #      / \
    #     2   4
    #    /
    #   1
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)

    # Test case 3
    k = 3
    result = solution.kthSmallest(root2, k)
    assert result == 3, f"Expected 3, got {result}"
    print(f"k={k}: {result}")

    print("All tests passed!")


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Find kth smallest element in BST.

        BST inorder traversal gives sorted order: left -> root -> right

        Time: O(H + k) where H is tree height
        Space: O(H) for recursion stack
        """
        # Collect values in sorted order via inorder traversal
        values = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return values[k - 1]


if __name__ == '__main__':
    main()
