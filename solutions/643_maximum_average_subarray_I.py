from typing import List


def main():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    print(result)


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = max_sum = sum(nums[:k])  # To calculate the first sum

        for i in range(0, len(nums)-k):
            cur_sum = cur_sum - nums[i] + nums[i+k]  # Sliding window
            max_sum = max(max_sum, cur_sum)

        return max_sum/k


if __name__ == '__main__':
    main()
