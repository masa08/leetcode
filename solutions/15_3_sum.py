def main():
    solution = Solution()

    # Basic cases
    assert solution.threeSum([-1, 0, 1, 2, -1, -4]
                             ) == [[-1, -1, 2], [-1, 0, 1]]
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]

    # Edge cases
    assert solution.threeSum([0, 1, 1]) == []
    assert solution.threeSum([1, -1, -1, 0]) == [[-1, 0, 1]]

    print("All tests passed!")


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Sort + Two Pointers.
        Fix one element, then use two pointers on the remaining sorted subarray.
        Skip duplicates at both the outer loop and inner loop to avoid repeated triplets.

        Time: O(n²) - outer loop O(n) × two pointers O(n)
        Space: O(1) - excluding the output array (sort is in-place)
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return result


if __name__ == '__main__':
    main()
