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
        graph = defaultdict(dict)
        for (A, B), value in zip(equations, values):
            graph[A][B] = value
            graph[B][A] = 1 / value

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0

            """Base case
            例えば、start = "A", end = "B" の場合、
            graph["A"] = {"B": 2.0} となっているので、
            neighbor = "B" となり、
            result = dfs("B", "B", visited) となる。
            つまり、start == end となる。
            このとき、1.0 を返す。
            """
            if start == end:
                return 1.0

            visited.add(start)
            for neighbor in graph[start]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return graph[start][neighbor] * result

            return -1.0

        results = []
        for C, D in queries:
            results.append(dfs(C, D, set()))

        return results


if __name__ == '__main__':
    main()
