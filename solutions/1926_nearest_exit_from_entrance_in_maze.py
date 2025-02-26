from typing import List


def main():
    args = [
        [["+", "+", ".", "+"], [".", ".", "+", "+"],
            ["+", ".", ".", "+"], ["+", "+", "+", "."]],
        [1, 2],
    ]
    solution = Solution()
    result = solution.nearestExit(args[0], args[1])
    print(result)


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = [(entrance[0], entrance[1], 0)]
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            x, y, steps = queue.pop(0)

            if (x == 0 or x == m-1 or y == 0 or y == n-1) and (x, y) != (entrance[0], entrance[1]):
                return steps

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))

        return -1


if __name__ == '__main__':
    main()
