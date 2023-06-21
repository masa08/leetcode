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
        rotten = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r, c])
                elif grid[r][c] == 1:
                    fresh_count += 1

        minutes_passed = 0
        while rotten and fresh_count > 0:
            minutes_passed += 1
            for _ in range(len(rotten)):
                row, col = rotten.pop(0)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    neighbor_row, neighbor_col = row + dx, col + dy
                    if neighbor_row < 0 or neighbor_row >= rows or neighbor_col < 0 or neighbor_col >= cols:
                        continue
                    if grid[neighbor_row][neighbor_col] == 0 or grid[neighbor_row][neighbor_col] == 2:
                        continue

                    fresh_count -= 1
                    grid[neighbor_row][neighbor_col] = 2
                    rotten.append([neighbor_row, neighbor_col])

        return minutes_passed if fresh_count == 0 else -1


if __name__ == '__main__':
    main()
