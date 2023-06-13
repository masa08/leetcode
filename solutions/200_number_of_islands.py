from typing import List


def main():
    args = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    solution = Solution()
    result = solution.numIslandsBfs(args)
    print(result)


class Solution:
    # dfs
    def numIslandsDfs(self, grid: List[List[str]]) -> int:
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
    def numIslandsBfs(self, grid: List[List[str]]) -> int:
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
