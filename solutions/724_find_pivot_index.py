from typing import List


def main():
    args = [1, 7, 3, 6, 5, 6]
    solution = Solution()
    result = solution.pivotIndex(args)
    print(result)


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i in range(len(nums)):
            if (i != 0):
                left_sum += nums[i-1]
            right_sum -= nums[i]
            if (left_sum == right_sum):
                return i

        return -1


if __name__ == '__main__':
    main()
