from collections import deque
from typing import List


def main():
    solution = Solution()

    # Basic case - rot spreads to all oranges
    assert solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4

    # Edge case - no fresh oranges
    assert solution.orangesRotting([[2]]) == 0

    # Edge case - isolated fresh orange (impossible to rot)
    assert solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1

    print("All tests passed!")


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS (Multi-source BFS)
        - Start BFS from all initially rotten oranges
        - Each minute, rot spreads to adjacent fresh oranges

        Time Complexity: O(rows * cols) - visit each cell at most once
        Space Complexity: O(rows * cols) - queue can hold up to all cells
        """
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
