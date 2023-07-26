from typing import List


def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums = sorted(nums)
        left, right = 0, len(nums)-1

        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1

        return count


if __name__ == '__main__':
    main()
