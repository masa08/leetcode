from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Edge cases
        if len(nums) == 1:
            return nums[0]

        # Binary search approach O(log n)
        left, right = 0, len(nums) - 1

        # If array is not rotated
        if nums[right] > nums[left]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than right element,
            # minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum is in left half (including mid)
                right = mid

        return nums[left]


def main():
    solution = Solution()

    # Basic cases
    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([11, 13, 15, 17]) == 11

    # Edge cases
    assert solution.findMin([1]) == 1
    assert solution.findMin([2, 1]) == 1

    print("All tests passed!")


if __name__ == "__main__":
    main()
