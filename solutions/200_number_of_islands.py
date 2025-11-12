from typing import List


def main():
    solution = Solution()

    # DFS tests
    # Basic case
    grid1 = [["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]
    assert solution.numIslandsDfs(grid1) == 2

    # Single island
    grid2 = [["1", "1"], ["1", "1"]]
    assert solution.numIslandsDfs(grid2) == 1

    # No islands
    grid3 = [["0", "0"], ["0", "0"]]
    assert solution.numIslandsDfs(grid3) == 0

    # BFS tests
    # Basic case
    grid4 = [["1", "1", "0"], ["1", "0", "0"], ["0", "0", "1"]]
    assert solution.numIslandsBfs(grid4) == 2

    # Single island
    grid5 = [["1", "1"], ["1", "1"]]
    assert solution.numIslandsBfs(grid5) == 1

    # No islands
    grid6 = [["0", "0"], ["0", "0"]]
    assert solution.numIslandsBfs(grid6) == 0

    print("All tests passed!")


class Solution:
    def numIslandsDfs(self, grid: List[List[str]]) -> int:
        """
        DFS approach: Mark visited cells as "0" to avoid revisiting
        Time: O(m*n) - visit each cell once
        Space: O(m*n) - worst case recursion depth when entire grid is one island
        """
        def _dfs(grid, r, c):
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])):
                return
            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            _dfs(grid, r-1, c)
            _dfs(grid, r+1, c)
            _dfs(grid, r, c+1)
            _dfs(grid, r, c-1)

        rows = len(grid)
        columns = len(grid[0])
        result = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    result += 1
                    _dfs(grid, r, c)

        return result

    def numIslandsBfs(self, grid: List[List[str]]) -> int:
        """
        BFS approach: Use queue to explore connected cells level by level
        Time: O(m*n) - visit each cell once
        Space: O(min(m,n)) - queue holds "wave front" of BFS traversal
               Maximum queue size limited by grid's shorter dimension
        """
        def _bfs(grid, r, c):
            queue = [[r, c]]

            while len(queue) != 0:
                r, c = queue.pop(0)

                if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])):
                    continue
                if grid[r][c] == "0":
                    continue

                grid[r][c] = "0"
                queue.append([r-1, c])
                queue.append([r+1, c])
                queue.append([r, c+1])
                queue.append([r, c-1])

        rows = len(grid)
        columns = len(grid[0])
        result = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    result += 1
                    _bfs(grid, r, c)

        return result


if __name__ == '__main__':
    main()
