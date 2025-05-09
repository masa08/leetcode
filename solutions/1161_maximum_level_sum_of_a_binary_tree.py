from collections import defaultdict
from typing import Optional

from model import TreeNode
from utils import makeTree


def main():
    # Manually construct the binary tree
    args = [1, 7, 0, 7, -8, None, None]
    root = makeTree(args)

    # Solve the problem
    solution = Solution()
    result = solution.maxLevelSum(root)
    print(result)


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        max_sum, answer, cur_level = root.val, 1, 1

        while queue:
            total = 0

            for _ in range(0, len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                total += node.val

            if max_sum < total:
                max_sum, answer = total, cur_level
            cur_level += 1

        return answer

        # def bfs(root):
        #     queue = [root]
        #     level = 1

        #     while queue:
        #         val = 0
        #         for _ in range(0, len(queue)):
        #             node = queue.pop(0)
        #             if node.left:
        #                 queue.append(node.left)
        #             if node.right:
        #                 queue.append(node.right)
        #             val += node.val

        #         level_value[level] = val
        #         level += 1

        # level_value = defaultdict(int)
        # bfs(root)

        # return max(level_value, key=level_value.get)


if __name__ == '__main__':
    main()
