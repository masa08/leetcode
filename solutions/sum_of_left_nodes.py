from typing import Optional


def main():
    pass
    # TODO: data生成
    # args = ""
    # solution = Solution()
    # result = solution.hoge()
    # print(result)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
