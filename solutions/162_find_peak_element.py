from typing import List


def main():
    args = [1, 2, 3, 1]
    solution = Solution()
    result = solution.findPeakElement(args)
    print(result)


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(log n)
        left, right = 0, len(nums)-1

        while left < right:
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot+1]:
                right = pivot
            else:
                left = pivot+1

        return left

        # O(n)
        # peak_elem = 0
        # for index, num in enumerate(nums):
        #     if num > nums[peak_elem]:
        #         peak_elem = index

        # return peak_elem


if __name__ == '__main__':
    main()
