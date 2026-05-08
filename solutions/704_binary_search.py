from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1

    # Edge cases
    assert solution.search([5], 5) == 0           # Single element, found
    assert solution.search([5], 0) == -1          # Single element, not found
    assert solution.search([1, 2, 3, 4, 5], 1) == 0   # First element
    assert solution.search([1, 2, 3, 4, 5], 5) == 4   # Last element

    print("All tests passed!")


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Standard binary search on a sorted array.
        Compare nums[mid] with target and halve the search range each step.

        Time: O(log n) - range halves each iteration
        Space: O(1) - only pointers
        """
        left, right = 0, len(nums) - 1

        # Use `<=` because right is inclusive (len-1).
        # If right were `len(nums)` (exclusive), use `<` instead.
        # With `<=`, a single-element array still enters the loop.
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


if __name__ == '__main__':
    main()
