from collections import deque
from typing import List


def main():
    solution = Solution()

    # DFS tests
    grid1 = [["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]
    assert solution.numIslands(grid1) == 2

    grid2 = [["1", "1"], ["1", "1"]]
    assert solution.numIslands(grid2) == 1

    grid3 = [["0", "0"], ["0", "0"]]
    assert solution.numIslands(grid3) == 0

    # BFS tests
    grid4 = [["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]
    assert solution.numIslands_bfs(grid4) == 2

    grid5 = [["1", "1"], ["1", "1"]]
    assert solution.numIslands_bfs(grid5) == 1

    grid6 = [["0", "0"], ["0", "0"]]
    assert solution.numIslands_bfs(grid6) == 0

    print("All tests passed!")


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS (recursive): for each unvisited '1', increment count and
        flood-fill the entire island by marking connected cells as '0'.

        Time: O(m*n) - visit each cell once
        Space: O(m*n) - worst case recursion depth when entire grid is one island
        """
        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                return
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    result += 1
                    dfs(r, c)

        return result

    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        """
        BFS (iterative): same logic as DFS but uses a deque to explore
        connected cells level by level.

        Time: O(m*n) - visit each cell once
        Space: O(min(m,n)) - queue holds BFS wave front
        """
        def bfs(r, c):
            queue = deque([(r, c)])
            while queue:
                r, c = queue.popleft()
                if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
                    continue
                if grid[r][c] == "0":
                    continue

                grid[r][c] = "0"
                queue.append((r - 1, c))
                queue.append((r + 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))

        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    result += 1
                    bfs(r, c)

        return result


if __name__ == '__main__':
    main()
