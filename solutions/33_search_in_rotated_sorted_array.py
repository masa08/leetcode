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
    def search(self, nums, target):
        """
        Search for target in rotated sorted array using binary search.
        Time: O(log n), Space: O(1)
        """
        if not nums:
            return -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Check if mid is the target
            if target == nums[mid]:
                return mid

            # Left half is sorted
            if nums[low] <= nums[mid]:
                # Target is in the sorted left half
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted (rotated)
            else:
                # Target is in the sorted right half
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


if __name__ == '__main__':
    main()
