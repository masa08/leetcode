from typing import Optional


def main():
    treenode = TreeNode(0)
    solution = Solution()
    result = solution.isSymmetric(treenode)
    print(result)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def _isSymmetric(first, second) -> bool:
            # どちらにも子要素がない場合
            if not first and not second:
                return True
            # 片方の子要素がない場合
            if not first or not second:
                return False
            # 双方子要素がある場合
            if first.val != second.val:
                return False

            return _isSymmetric(first.left, second.right) and _isSymmetric(first.right, second.left)

        if not root:
            return True
        return _isSymmetric(root.left, root.right)


if __name__ == '__main__':
    main()
