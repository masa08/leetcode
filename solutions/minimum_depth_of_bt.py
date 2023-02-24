
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def main():
    # TODO: inputデータの作成
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
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

        # DFS
        # if not root: return 0
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)

        # if left == 0: return 1 + right
        # if right == 0: return 1 + left

        # return 1 + min(left, right)


if __name__ == '__main__':
    main()
