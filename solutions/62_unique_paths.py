def main():
    m = 3
    n = 7
    solution = Solution()
    result = solution.uniquePaths(m, n)
    print(result)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D list (dp) with 1s, representing the number of ways to reach each cell
        dp = [[1] * n for _ in range(m)]

        # Iterate over each cell starting from the second row and second column
        # because the first row and the first column are already initialized to 1
        for row in range(1, m):
            for col in range(1, n):
                # The number of ways to reach the current cell is the sum of the ways to reach
                # the cell directly above it and the cell directly to the left of it
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        # Return the number of ways to reach the bottom-right corner of the grid
        return dp[m-1][n-1]


if __name__ == '__main__':
    main()
