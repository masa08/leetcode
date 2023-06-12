from typing import List


def main():
    args = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    solution = Solution()
    result = solution.numIslands(args)
    print(result)


class Solution:
    # dfs
    def numIslands(self, grid: List[List[str]]) -> int:
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

    # bfs


if __name__ == '__main__':
    main()
