def main():
    solution = Solution()

    # Basic cases
    assert solution.uniquePaths(3, 7) == 28
    assert solution.uniquePaths(3, 2) == 3

    # Edge cases
    assert solution.uniquePaths(1, 1) == 1  # 1x1 grid
    assert solution.uniquePaths(1, 5) == 1  # 1 row
    assert solution.uniquePaths(5, 1) == 1  # 1 col

    print("All tests passed!")


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        2D DP: dp[r][c] = number of paths to reach cell (r, c).
        First row and first column are all 1 (only one way to reach them).
        Each cell = sum of cell above + cell to the left.

        Time: O(m*n) - fill every cell once
        Space: O(m*n) - dp table
        """
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[-1][-1]


if __name__ == '__main__':
    main()
