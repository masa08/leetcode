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
        # Edge case: empty tree
        if not root:
            return None

        # DFS approach (Recursive) - PREFERRED for this problem
        # - Swap left and right children at each node
        # - Recursively invert left and right subtrees
        # - Time: O(n), Space: O(h) where h is height (call stack)
        # - WHY DFS?: Simple, intuitive - matches tree structure naturally
        #   Space is better for balanced trees: O(log n) vs O(n/2) for BFS

        # Swap children
        root.left, root.right = root.right, root.left

        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        # BFS approach (Iterative)
        # - Process nodes level by level using queue
        # - Swap children at each node
        # - Time: O(n), Space: O(w) where w is max width
        # - Use when: Prefer iterative solution or need level-order processing
        # queue = [root]
        # while queue:
        #     node = queue.pop(0)
        #     if node:
        #         # Swap children
        #         node.left, node.right = node.right, node.left
        #         # Add children to queue
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root


if __name__ == '__main__':
    main()
