from typing import List, Optional

from model import TreeNode


def main():
    # Create test data: Binary tree
    # Example tree:
    #        1
    #       / \
    #      2   3
    #       \    \
    #        5    4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    # Apply the solution
    solution = Solution()
    result = solution.rightSideView(root)

    # Print the result
    print(f"Right side view: {result}")


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return result


if __name__ == '__main__':
    main()
