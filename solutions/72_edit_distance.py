def main():
    solution = Solution()

    # Basic cases
    assert solution.minDistance("horse", "ros") == 3
    assert solution.minDistance("intention", "execution") == 5

    # Edge cases
    assert solution.minDistance("", "") == 0
    assert solution.minDistance("", "abc") == 3   # 3 insertions
    assert solution.minDistance("abc", "") == 3   # 3 deletions
    assert solution.minDistance("a", "a") == 0    # Same character

    print("All tests passed!")


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        2D DP: dp[i][j] = min operations to convert word1[:i] to word2[:j].
        If characters match, no operation needed (take diagonal).
        If not, take 1 + min of three operations:
          - diagonal (replace), above (delete), left (insert).

        Time: O(m*n) - fill every cell once
        Space: O(m*n) - dp table
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j - 1] + 1,  # replace
                        dp[i - 1][j] + 1,       # delete
                        dp[i][j - 1] + 1,       # insert
                    )

        return dp[-1][-1]


if __name__ == '__main__':
    main()
