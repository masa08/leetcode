from typing import List


def main():
    args = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    result = solution.maxSubArray(args)
    print(result)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_num = ans = nums[0]

        for i in range(1, n):
            curr_num = max(nums[i], curr_num + nums[i])
            ans = max(curr_num, ans)

        return ans


if __name__ == '__main__':
    main()
