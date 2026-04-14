def main():
    solution = Solution()

    # Basic cases
    assert solution.longestCommonSubsequence("abcde", "ace") == 3
    assert solution.longestCommonSubsequence("abc", "abc") == 3
    assert solution.longestCommonSubsequence("abc", "def") == 0

    # Edge cases
    assert solution.longestCommonSubsequence("", "abc") == 0
    assert solution.longestCommonSubsequence("a", "a") == 1

    print("All tests passed!")


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        2D DP: dp[i][j] = LCS length of text1[:i] and text2[:j].
        If characters match, take diagonal + 1.
        If not, take max of cell above or cell to the left.

        Time: O(m*n) - fill every cell once
        Space: O(m*n) - dp table
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    main()
