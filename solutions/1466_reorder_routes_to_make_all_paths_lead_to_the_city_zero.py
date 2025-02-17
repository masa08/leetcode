from collections import defaultdict


def main():
    args = (6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
    solution = Solution()
    result = solution.minReorder(*args)
    print(result)


class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        graph = defaultdict(list)
        edges = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            edges.add((a, b))

        # def dfs(city, parent):
        #     changes = 0
        #     for neighbor in graph[city]:
        #         if neighbor == parent:
        #             continue

        #         if (city, neighbor) in edges:
        #             changes += 1

        #         changes += dfs(neighbor, city)
        #     return changes

        # return dfs(0, -1)

        def bfs(city, parent):
            changes = 0
            queue = [(city, parent)]

            while queue:
                city, parent = queue.pop(0)
                for neighbor in graph[city]:
                    if neighbor == parent:
                        continue

                    if (city, neighbor) in edges:
                        changes += 1

                    queue.append((neighbor, city))

            return changes

        return bfs(0, -1)


if __name__ == '__main__':
    main()
