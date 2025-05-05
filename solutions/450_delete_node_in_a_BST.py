from common import TreeNode
from typing import Optional


def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    # Key to delete
    key = 3

    # Apply the solution
    solution = Solution()
    result = solution.deleteNode(root, key)

    # Print the resulting tree in-order
    def inorder_traversal(node):
        if not node:
            return []
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)

    print(f"BST after deleting {key}: {inorder_traversal(result)}")


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root

    def successor(self, root: TreeNode) -> TreeNode:
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root: TreeNode) -> TreeNode:
        root = root.left
        while root.right:
            root = root.right
        return root.val


if __name__ == '__main__':
    main()
