# TODO: Fix bug in the code
from typing import Optional

from model import TreeNode


def main():
    args = [1, 2, 2, 1, 1, 3]
    solution = Solution()
    result = solution.uniqueOccurrences(args)
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
