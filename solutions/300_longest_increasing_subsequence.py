from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4

    # Edge cases
    assert solution.lengthOfLIS([7, 7, 7, 7, 7]) == 1  # All same
    assert solution.lengthOfLIS([1]) == 1               # Single element
    assert solution.lengthOfLIS([1, 2, 3, 4, 5]) == 5   # Already sorted

    print("All tests passed!")


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        1D DP: dp[i] = length of LIS ending at index i.
        For each element, compare with all previous elements.
        If nums[i] > nums[j], we can extend the subsequence ending at j.

        Time: O(n^2) - nested loops
        Space: O(n) - dp array
        """
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    main()
