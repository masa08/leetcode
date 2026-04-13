from typing import Optional

from model import TreeNode
from utils import makeTree


def main():
    solution = Solution()

    # Basic case
    assert solution.maxDepth(makeTree([3, 9, 20, None, None, 15, 7])) == 3

    # Edge cases
    assert solution.maxDepth(None) == 0
    assert solution.maxDepth(makeTree([1])) == 1

    print("All tests passed!")


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        DFS (recursive): depth = 1 + max(left depth, right depth).
        Alternative: BFS counting levels with a queue - see maxDepth_bfs below.

        Time: O(n) - visit each node once
        Space: O(h) - recursion call stack, h = height of tree
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth_bfs(self, root: Optional[TreeNode]) -> int:
        """
        BFS (iterative): process nodes level by level, count depth.

        Time: O(n) - visit each node once
        Space: O(w) - queue stores at most one level, w = max width
        """
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1

        return depth


if __name__ == '__main__':
    main()
