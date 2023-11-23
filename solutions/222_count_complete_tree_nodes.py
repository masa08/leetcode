from typing import Optional


def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        count = 0
        queue = [root]

        while queue:
            node = queue.pop(0)
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return count


if __name__ == '__main__':
    main()
