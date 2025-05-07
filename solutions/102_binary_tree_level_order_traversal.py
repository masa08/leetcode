from model import TreeNode
from typing import List, Optional


def main():
    # Convert array to BST
    args = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(args[0])
    root.left = TreeNode(args[1])
    root.right = TreeNode(args[2])
    root.right.left = TreeNode(args[5])
    root.right.right = TreeNode(args[6])

    # Solve the problem
    solution = Solution()
    result = solution.levelOrder(root)
    print(result)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if root is None:
            return []
        q = [root]
        result = []

        while q:
            temp = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node:
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            result.append(temp)

        return result


if __name__ == '__main__':
    main()
