from collections import deque
from typing import List


def main():
    args = [[2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647]]
    solution = Solution()
    result = solution.wallsAndGates(args)
    print(result)


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        while queue:
            row, col = queue.popleft()
            for dx, dy in directions:
                nr, nc = row + dx, col + dy
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                    rooms[nr][nc] = rooms[row][col] + 1
                    queue.append((nr, nc))

        return rooms


if __name__ == '__main__':
    main()
