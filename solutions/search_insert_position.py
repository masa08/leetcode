# ref: https://leetcode.com/problems/search-insert-position/solutions/525270/search-insert-position/?orderBy=most_votes
from typing import List


def main():
    nums = [1, 3, 5, 6]
    target = 5
    solution = Solution()
    result = solution.searchInsert(nums, target)

    print(result)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # if the target value is not found,
        # we can return left
        # because the loop will be stopped
        # when right < left and nums[right] < target < nums[left]
        return left


if __name__ == "__main__":
    main()
