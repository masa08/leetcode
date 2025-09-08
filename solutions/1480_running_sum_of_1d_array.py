from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert solution.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert solution.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]

    # エッジケース
    assert solution.runningSum([1]) == [1]
    assert solution.runningSum([0, 0, 0]) == [0, 0, 0]
    assert solution.runningSum([-1, -2, -3]) == [-1, -3, -6]

    print("All tests passed!")


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        running_sum = [0] * n
        running_sum[0] = nums[0]

        for i in range(1, n):
            running_sum[i] = running_sum[i-1] + nums[i]

        return running_sum

        # n = len(nums)
        # cumulative_sum = [0] * (n+1)

        # for i in range(n):
        #     cumulative_sum[i+1] = nums[i] + cumulative_sum[i]

        # return cumulative_sum[1::]


if __name__ == '__main__':
    main()
