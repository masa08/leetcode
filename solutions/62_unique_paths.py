def main():
    m = 3
    n = 7
    solution = Solution()
    result = solution.uniquePaths(m, n)
    print(result)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]


if __name__ == '__main__':
    main()
