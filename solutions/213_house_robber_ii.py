from typing import List


def main():
    args = [1, 2, 3, 1]
    solution = Solution()
    result = solution.rob(args)
    print(result)


class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses: List[int]) -> int:
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            return dp[-1]

        if len(nums) == 0:
            return 0

        if len(nums) <= 3:
            return max(nums)

        dp1 = rob_linear(nums[1:])
        dp2 = rob_linear(nums[:-1])

        return max(dp1, dp2)


if __name__ == '__main__':
    main()
