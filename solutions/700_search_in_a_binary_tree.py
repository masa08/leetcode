from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    # TODO: treeを配列から作成する
    args = [4, 2, 7, 1, 3]
    solution = Solution()
    result = solution.searchBST(args, 2)
    print(result)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def _searchBST(root, val):
            if root is None:
                return None
            if root.val == val:
                return root

            if val < root.val:
                return _searchBST(root.left, val)
            else:
                return _searchBST(root.right, val)

        return _searchBST(root, val)


if __name__ == '__main__':
    main()
