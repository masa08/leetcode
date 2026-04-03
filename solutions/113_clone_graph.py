from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        queue = deque([node])

        while queue:
            cur_node = queue.popleft()

            for nei in cur_node.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    queue.append(nei)
                # initialize the neighbors of the current node
                old_to_new[cur_node].neighbors.append(old_to_new[nei])

        return old_to_new[node]


if __name__ == '__main__':
    main()
