from collections import defaultdict
from typing import Optional


def main():
    args = [1, 7, 0, 7, -8, None, None]
    solution = Solution()
    result = solution.maxLevelSum(args)
    print(result)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def bfs(root):
            queue = [root]
            level = 1

            while queue:
                val = 0
                for _ in range(0, len(queue)):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    val += node.val

                level_value[level] = val
                level += 1

        level_value = defaultdict(int)
        bfs(root)

        return max(level_value, key=level_value.get)


if __name__ == '__main__':
    main()
