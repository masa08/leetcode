from typing import List


def main():
    solution = Solution()

    # Basic case
    assert solution.rob([2, 3, 2]) == 3
    assert solution.rob([1, 2, 3, 1]) == 4

    # Edge cases
    assert solution.rob([1]) == 1
    assert solution.rob([1, 2]) == 2

    print("All tests passed!")


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        House Robber II - Circular array variation

        Approach: Split into two linear House Robber problems
        - Case 1: Rob houses[1:] (exclude first house)
        - Case 2: Rob houses[:-1] (exclude last house)
        - Return max of both cases

        Time Complexity: O(n)
        Space Complexity: O(n) for dp array
        """
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

        # WHY split into two cases?
        # Since houses are arranged in a circle, first and last house are neighbors
        # We cannot rob both first and last house at the same time
        # So we solve two separate linear problems and take the max:

        # Case 1: Exclude first house (index 0), rob from houses[1:]
        # This means we CAN rob the last house if needed
        dp1 = rob_linear(nums[1:])

        # Case 2: Exclude last house (index n-1), rob from houses[:-1]
        # This means we CAN rob the first house if needed
        dp2 = rob_linear(nums[:-1])

        # Return the maximum profit from both scenarios
        return max(dp1, dp2)


if __name__ == '__main__':
    main()
