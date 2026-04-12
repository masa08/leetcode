from typing import Optional

from model import TreeNode
from utils import makeTree


def main():
    solution = Solution()

    # Basic cases
    root1 = makeTree([4, 2, 7, 1, 3, 6, 9])
    solution.invertTree(root1)
    assert root1.val == 4
    assert root1.left.val == 7
    assert root1.right.val == 2

    root2 = makeTree([2, 1, 3])
    solution.invertTree(root2)
    assert root2.val == 2
    assert root2.left.val == 3
    assert root2.right.val == 1

    # Edge cases
    assert solution.invertTree(None) is None

    root3 = makeTree([1])
    solution.invertTree(root3)
    assert root3.val == 1

    print("All tests passed!")


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        DFS (recursive): swap left and right children at each node, then recurse.
        Alternative: BFS with queue - see invertTree_bfs below.

        Time: O(n) - visit each node once
        Space: O(h) - recursion call stack, h = height of tree
        """
        if not root:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree_bfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        BFS (iterative): swap children level by level using a queue.

        Time: O(n) - visit each node once
        Space: O(w) - queue stores at most one level, w = max width
        """
        if not root:
            return None

        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


if __name__ == '__main__':
    main()
