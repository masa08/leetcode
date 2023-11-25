from typing import List, Optional


def main():
    args = [1, 2, 3, None, 5]
    solution = Solution()
    result = solution.binaryTreePaths(args)
    print(result)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def _def(self, root, paths):
            paths += str(root.val)

            # leaf node
            if root.left is None and root.right is None:
                res.append(paths)

            if root.left:
                new_paths = paths + "->"
                _def(self, root.left, new_paths)
            if root.right:
                new_paths = paths + "->"
                _def(self, root.right, new_paths)

        _def(self, root, "")

        return res


if __name__ == '__main__':
    main()
