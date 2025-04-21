from collections import deque
from typing import List


def main():
    args = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    solution = Solution()
    result = solution.orangesRotting(args)
    print(result)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        fresh_oranges_count = 0
        passed_minutes = 0
        rotting_oranges = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotting_oranges.append((r, c))
                if grid[r][c] == 1:
                    fresh_oranges_count += 1

        while rotting_oranges and fresh_oranges_count > 0:
            passed_minutes += 1
            for _ in range(len(rotting_oranges)):
                row, col = rotting_oranges.popleft()
                for dx, dy in directions:
                    nx, ny = row + dx, col + dy
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue
                    if grid[nx][ny] == 1:
                        fresh_oranges_count -= 1
                        grid[nx][ny] = 2
                        rotting_oranges.append((nx, ny))

        return passed_minutes if fresh_oranges_count == 0 else -1


if __name__ == '__main__':
    main()
