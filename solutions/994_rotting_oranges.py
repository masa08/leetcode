from typing import List


def main():
    args = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    solution = Solution()
    result = solution.orangesRotting(args)
    print(result)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        minutes_passed = 0
        # Initialize an array to store the rotten oranges
        rotten = []

        # Traverse the grid to find rotten and fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r, c])
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Directions for the 4 possible movements (up, down, left, right)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Perform BFS to rot adjacent fresh oranges
        while rotten and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                x, y = rotten.pop(0)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                        continue
                    if grid[nx][ny] == 1:
                        fresh_count -= 1
                        grid[nx][ny] = 2
                        rotten.append([nx, ny])

        return minutes_passed if fresh_count == 0 else -1


if __name__ == '__main__':
    main()
