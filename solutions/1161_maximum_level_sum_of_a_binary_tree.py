from collections import defaultdict
from typing import Optional

from model import TreeNode
from utils import makeTree


def main():
    solution = Solution()

    # Basic case
    root1 = makeTree([1, 7, 0, 7, -8, None, None])
    assert solution.maxLevelSum(root1) == 2

    # Edge case: single node
    root2 = makeTree([1])
    assert solution.maxLevelSum(root2) == 1

    # Edge case: negative values
    root3 = makeTree([-100, -200, -300, -20, -5, -10, None])
    assert solution.maxLevelSum(root3) == 3

    print("All tests passed!")


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        BFS (Level-order traversal) to find the level with maximum sum.

        Algorithm:
        - Use a queue to traverse the tree level by level
        - For each level, calculate the sum of all node values
        - Track the level with the maximum sum

        Time Complexity: O(n) - visit each node once
        Space Complexity: O(w) - w is the maximum width of the tree (queue size)
        """
        queue = [root]
        max_sum, answer, level = root.val, 1, 1

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
                max_sum, answer = total, level
            level += 1

        return answer


if __name__ == '__main__':
    main()
