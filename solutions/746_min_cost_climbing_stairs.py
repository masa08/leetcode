from typing import List


def main():
    args = [10, 15, 20]
    solution = Solution()
    result = solution.minCostClimbingStairs(args)
    print(result)


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(cost[i]+dp[i-2], cost[i]+dp[i-1])

        return min(dp[len(cost)-1], dp[len(cost)-2])


if __name__ == '__main__':
    main()
