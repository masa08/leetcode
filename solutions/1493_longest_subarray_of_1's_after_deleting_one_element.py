from typing import List


def main():
    args = [1, 1, 0, 1]
    solution = Solution()
    result = solution.longestSubarray(args)
    print(result)


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroCount = 0
        longestWindow = 0
        start = 0

        for i, num in enumerate(nums):
            zeroCount += 1 if num == 0 else 0
            while zeroCount > 1:
                zeroCount -= 1 if nums[start] == 0 else 0
                start += 1

            longestWindow = max(longestWindow, i - start)

        return longestWindow


if __name__ == '__main__':
    main()
