from typing import Optional

from model import TreeNode
from utils import makeTree


def main():
    args1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    root1 = makeTree(args1)
    args2 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    root2 = makeTree(args2)

    solution = Solution()
    result = solution.leafSimilar(root1, root2)
    print(result)


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def extract(root, result):
            if root is None:
                return
            if root.left is None and root.right is None:
                result.append(root.val)
            else:
                extract(root.left, result)
                extract(root.right, result)

        rootLeaf1 = []
        rootLeaf2 = []
        extract(root1, rootLeaf1)
        extract(root2, rootLeaf2)

        return rootLeaf1 == rootLeaf2


if __name__ == '__main__':
    main()
