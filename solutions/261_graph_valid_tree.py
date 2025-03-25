from collections import defaultdict
from typing import List


def main():
    args = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]
    solution = Solution()
    result = solution.validTree(*args)
    print(result)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def hasCycle(current: int, parent: int) -> bool:
            if current in visited:
                return True

            visited.add(current)
            for neighbor in graph[current]:
                if neighbor == parent:
                    continue

                result = hasCycle(neighbor, current)
                if result:
                    return True

            return False

        contains_cycle = hasCycle(0, -1)
        is_connected = len(visited) == n

        return not contains_cycle and is_connected


if __name__ == '__main__':
    main()
