# TODO: Fix bug in the code
from common import TreeNode
from typing import List, Optional


def main():
    args = [3, 9, 20, None, None, 15, 7]
    solution = Solution()
    result = solution.levelOrder(args)
    print(result)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if root is None:
            return []
        q = [root]
        result = []

        while q:
            temp = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            result.append(temp)

        return result


if __name__ == '__main__':
    main()
