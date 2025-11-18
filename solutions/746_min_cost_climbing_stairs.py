from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.minCostClimbingStairs([10, 15, 20]) == 15
    assert solution.minCostClimbingStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6

    # Edge cases
    assert solution.minCostClimbingStairs([0, 0]) == 0
    assert solution.minCostClimbingStairs([1, 1]) == 1

    print("All tests passed!")


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Dynamic Programming approach
        - At each step, choose minimum cost from (i-1)th or (i-2)th step
        - dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        - Final answer is min of last two steps (can reach top from either)

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(cost[i]+dp[i-2], cost[i]+dp[i-1])

        return min(dp[len(cost)-1], dp[len(cost)-2])


if __name__ == '__main__':
    main()
