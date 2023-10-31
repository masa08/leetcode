from typing import List


def main():
    args = [1, 2, 3, 1]
    solution = Solution()
    result = solution.rob(args)
    print(result)


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]

        for i in range(2, n):
            val = max(dp[:i-1])
            dp[i] = nums[i] + val

        return max(dp)


if __name__ == '__main__':
    main()
