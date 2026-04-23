from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.coinChange([1, 2, 5], 11) == 3   # 5+5+1
    assert solution.coinChange([2], 3) == -1          # Impossible

    # Edge cases
    assert solution.coinChange([1], 0) == 0           # Amount 0
    assert solution.coinChange([1], 1) == 1           # Single coin
    assert solution.coinChange([1, 2, 5], 100) == 20  # 5*20

    print("All tests passed!")


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        1D DP: dp[i] = min coins to make amount i.
        For each amount, try each coin as the last coin used.
        dp[i] = min(dp[i - coin] + 1) for each valid coin.

        Time: O(amount * n) - n = number of coin types
        Space: O(amount) - dp array
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    main()
