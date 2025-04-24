from collections import defaultdict
from typing import List


def main():
    args = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]
    solution = Solution()
    result = solution.countComponents(*args)
    print(result)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = [False] * n

        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        def _dfs(edge_index):
            visited[edge_index] = True
            for neighbor in graph[edge_index]:
                if not visited[neighbor]:
                    _dfs(neighbor)

        for i in range(n):
            if visited[i] == False:
                count += 1
                _dfs(i)

        return count


if __name__ == '__main__':
    main()
