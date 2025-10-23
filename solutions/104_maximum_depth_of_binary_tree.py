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
        if not root:
            return 0

        # DFS approach (Recursive) - PREFERRED for this problem
        # - Visit left and right subtrees recursively
        # - Return 1 + max depth of subtrees
        # - Time: O(n), Space: O(h) where h is height (call stack)
        # - WHY DFS?: Simpler code, naturally fits "depth" concept
        #   Space is better for balanced trees: O(log n) vs O(n/2) for BFS
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS approach (Iterative)
        # - Process nodes level by level using queue
        # - Count depth by tracking each level
        # - Time: O(n), Space: O(w) where w is max width
        # - Use when: Need level-order processing (not just depth)
        # queue = [root]
        # depth = 0
        # while queue:
        #     for _ in range(len(queue)):
        #         q = queue.pop(0)
        #         if q and q.left:
        #             queue.append(q.left)
        #         if q and q.right:
        #             queue.append(q.right)
        #     depth += 1
        # return depth


if __name__ == '__main__':
    main()
