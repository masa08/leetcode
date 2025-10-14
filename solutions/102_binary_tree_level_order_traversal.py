from model import TreeNode
from typing import List, Optional

from utils import makeTree


def main():
    solution = Solution()

    # Basic case
    root = makeTree([3, 9, 20, None, None, 15, 7])
    assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]

    # Edge case: empty tree
    assert solution.levelOrder(None) == []

    # Edge case: single node
    root = makeTree([1])
    assert solution.levelOrder(root) == [[1]]

    print("All tests passed!")


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
