from collections import defaultdict
from typing import List


def main():
    args = [1, 2, 3, 4, 5]
    k = 5
    solution = Solution()
    result = solution.maxSubArrayLen(args, k)
    print(result)


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_len, prefix_sum = 0, 0
        sum_dict = defaultdict(int)
        sum_dict[0] = -1

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum - k in sum_dict:
                curr_len = i - sum_dict[prefix_sum - k]
                max_len = max(max_len, curr_len)

            if prefix_sum not in sum_dict:
                sum_dict[prefix_sum] = i

        return max_len


if __name__ == '__main__':
    main()
