from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def main():
    # TODO: 生成対応
    # args = [3, 9, 20, 2, 2, 15, 7]
    # solution = Solution()
    # result = solution.maxDepth()
    # print(result)
    pass


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        if not root:
            return 0
        queue = [root]
        depth = 0

        while queue:
            for _ in range(len(queue)):
                q = queue.pop(0)
                if q and q.left:
                    queue.append(q.left)
                if q and q.right:
                    queue.append(q.right)
            depth += 1

        return depth


if __name__ == '__main__':
    main()
