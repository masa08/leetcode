
from typing import Optional

from model import TreeNode


def main():
    solution = Solution()

    # Basic case
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert solution.minDepth(root) == 2

    # Edge case: empty
    assert solution.minDepth(None) == 0

    # Edge case: single node
    assert solution.minDepth(TreeNode(1)) == 1

    print("All tests passed!")


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS: Level-order traversal to find first leaf node
        # Time: O(n), Space: O(w) where w is max width of tree
        # Advantage: Early termination - stops at first leaf found
        # Since BFS explores level by level, the first leaf encountered
        # is guaranteed to be at minimum depth (no need to check deeper levels)
        if not root:
            return 0
        queue = [[root, 1]]

        while queue:
            node, level = queue.pop(0)
            if node:
                # if node is leef node.
                if not node.left and not node.right:
                    return level
                else:
                    queue.append([node.left, level+1])
                    queue.append([node.right, level+1])

        # DFS: Recursive depth-first traversal
        # Time: O(n), Space: O(h) where h is height
        # Disadvantage: Must explore all branches to completion
        # Cannot terminate early - needs to compare all paths to find minimum
        # if not root: return 0
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)

        # if left == 0: return 1 + right
        # if right == 0: return 1 + left

        # return 1 + min(left, right)


if __name__ == '__main__':
    main()
