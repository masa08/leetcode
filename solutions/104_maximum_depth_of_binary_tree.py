from typing import Optional

from model import TreeNode


def makeTree(args):
    nodes = [TreeNode(val) if val else None for val in args]
    for i, node in enumerate(nodes):
        if node:
            left = i * 2 + 1
            right = i * 2 + 2
            if left < len(nodes):
                node.left = nodes[left]
            if right < len(nodes):
                node.right = nodes[right]
    return nodes[0]


def main():
    args = [3, 9, 20, None, None, 15, 7]
    solution = Solution()
    result = solution.maxDepth(makeTree(args))
    print(result)
    pass


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # DFS approach
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS approach
        queue = [root]
        depth = 0
        while queue:
            for _ in range(len(queue)):
                q = queue.pop(0)
                if q and q.left:
                    queue.append(q.left)
                if q and q.right:
                    queue.append(q.right)
            depth += 1

        return depth


if __name__ == '__main__':
    main()
