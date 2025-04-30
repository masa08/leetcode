def main():
    args1 = "abcde"
    args2 = "ace"
    solution = Solution()
    result = solution.longestCommonSubsequence(args1, args2)
    print(result)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        for col in range(1, n+1):
            for row in range(1, m+1):
                if text2[col-1] == text1[row-1]:
                    dp[col][row] = 1 + dp[col-1][row-1]
                else:
                    dp[col][row] = max(dp[col-1][row], dp[col][row-1])

        return dp[n][m]

        # dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # for col in reversed(range(len(text2))):
        #     for row in reversed(range(len(text1))):
        #         if text2[col] == text1[row]:
        #             dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
        #         else:
        #             dp_grid[row][col] = max(
        #                 dp_grid[row + 1][col], dp_grid[row][col + 1])

        # return dp_grid[0][0]


if __name__ == '__main__':
    main()
