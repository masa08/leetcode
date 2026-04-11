from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    # Edge cases
    assert solution.search([], 5) == -1
    assert solution.search([1], 1) == 0

    print("All tests passed!")


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Modified binary search for rotated sorted array.

        Why modified?
          A normal binary search needs the array to be fully sorted so it can
          decide direction by comparing nums[mid] with target.
          A rotated array has ONE "break point" where the order is broken,
          so a simple nums[mid] vs target comparison is not enough.

        Key insight:
          When we split a rotated sorted array at mid, AT LEAST ONE half is
          guaranteed to be fully sorted. We can detect which half is sorted
          by checking nums[low] <= nums[mid].

          Example: [4, 5, 6, 7, 0, 1, 2]
                    L        M        H
            nums[L]=4 <= nums[M]=7 → left half [4,5,6,7] is sorted

          Example: [6, 7, 0, 1, 2, 4, 5]
                    L        M        H
            nums[L]=6 > nums[M]=1 → left half is broken → right half [1,2,4,5] is sorted

        Algorithm:
          1. Find mid. If nums[mid] == target, done.
          2. Detect which half is sorted.
          3. Check whether target lies in the sorted half's range.
             - If yes, search that half.
             - If no, search the other half.
          4. Repeat. Eventually the search range becomes fully sorted.

        Time: O(log n) - binary search halves the range each iteration
        Space: O(1) - only pointers
        """
        if not nums:
            return -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid

            # If nums[low] <= nums[mid], the left half [low..mid] is sorted.
            if nums[low] <= nums[mid]:
                # Check if target lies within the sorted left half's range.
                if nums[low] <= target < nums[mid]:
                    high = mid - 1   # Target is in the sorted left half
                else:
                    # Target must be in the (possibly broken) right half
                    low = mid + 1
            # Otherwise, the right half [mid..high] is sorted.
            else:
                # Check if target lies within the sorted right half's range.
                if nums[mid] < target <= nums[high]:
                    low = mid + 1    # Target is in the sorted right half
                else:
                    # Target must be in the (possibly broken) left half
                    high = mid - 1

        return -1


if __name__ == '__main__':
    main()
