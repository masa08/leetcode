def main():
    solution = Solution()

    # Basic cases
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3

    # Edge cases
    assert solution.climbStairs(1) == 1

    # Large case
    assert solution.climbStairs(5) == 8

    print("All tests passed!")


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Dynamic Programming approach
        - Each step can be reached from (i-1)th step or (i-2)th step
        - dp[i] = dp[i-1] + dp[i-2] (Fibonacci sequence)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if n == 1:
            return 1

        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]


if __name__ == '__main__':
    main()
