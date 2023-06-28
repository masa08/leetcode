from typing import List, Optional


def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
