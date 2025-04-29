from typing import List
from collections import defaultdict


def main():
    args = [
        [["a", "b"], ["b", "c"]],
        [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
    ]
    solution = Solution()
    result = solution.calcEquation(args[0], args[1], args[2])
    print(result)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Create a graph to store the equations and their values
        graph = defaultdict(dict)
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value

        # Depth-first search to find the result of each query
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor in graph[start]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    # Result is the product of start to neighbor and the result from neighbor to end
                    return graph[start][neighbor] * result

            return -1.0

        # Process each query
        results = []
        for C, D in queries:
            results.append(dfs(C, D, set()))

        return results


if __name__ == '__main__':
    main()
