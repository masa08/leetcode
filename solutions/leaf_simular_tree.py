from typing import Optional

from common import TreeNode


def main():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = [1, 3, 2]
    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)

    solution = Solution()
    result = solution.leafSimilar(root1, root2)
    print(result)


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1Leaf = []
        root2Leaf = []
        self.extractLeafNodes(root1, root1Leaf)
        self.extractLeafNodes(root2, root2Leaf)

        return root1Leaf == root2Leaf

    def extractLeafNodes(self, root, result):
        if root is None:
            return

        if root.left is None and root.right is None:
            result.append(root.val)
        else:
            self.extractLeafNodes(root.left, result)
            self.extractLeafNodes(root.right, result)


if __name__ == '__main__':
    main()
