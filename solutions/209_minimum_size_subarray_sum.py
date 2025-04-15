from typing import List


def main():
    solution = Solution()

    # Test case 1
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(f"Input: target={target}, nums={nums}")
    print(f"Output: {solution.minSubArrayLen(target, nums)}")  # Expected: 2


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = 0
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                min_len = min(min_len, right-left+1)
                curr_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    main()
