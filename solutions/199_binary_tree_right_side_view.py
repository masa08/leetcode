from typing import List, Optional

from model import TreeNode


def main():
    solution = Solution()

    # Basic case
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(4)
    assert solution.rightSideView(root1) == [1, 3, 4]

    # Edge case: empty tree
    assert solution.rightSideView(None) == []

    # Edge case: single node
    root2 = TreeNode(1)
    assert solution.rightSideView(root2) == [1]

    # Edge case: left-skewed tree
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    assert solution.rightSideView(root3) == [1, 2, 3]

    print("All tests passed!")


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS (Level-order traversal) to get the rightmost node at each level.

        Algorithm:
        - Use a queue to traverse the tree level by level
        - For each level, track the last node (rightmost visible node)
        - Add the last node's value to the result

        Time Complexity: O(n) - visit each node once
        Space Complexity: O(w) - w is the maximum width of the tree (queue size)
        """
        if not root:
            return []
        result = []
        queue = [root]

        while queue:
            count = len(queue)
            for i in range(len(queue)):
                node = queue.pop(0)
                if node is None:
                    continue
                if i == count-1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


if __name__ == '__main__':
    main()
