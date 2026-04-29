from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.missingNumber([3, 0, 1]) == 2
    assert solution.missingNumber([0, 1]) == 2
    assert solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8

    # Edge cases
    assert solution.missingNumber([0]) == 1   # Only 0 → missing 1
    assert solution.missingNumber([1]) == 0   # Only 1 → missing 0

    print("All tests passed!")


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Set-based: convert nums to a set for O(1) lookup, then iterate
        through [0, n] to find the missing number.

        Time: O(n) - building set + linear scan
        Space: O(n) - set of nums

        Alternative: sum formula n*(n+1)/2 - sum(nums) — O(n) time, O(1) space.
        Alternative: XOR all indices and values — O(n) time, O(1) space.
        """
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i


if __name__ == '__main__':
    main()
