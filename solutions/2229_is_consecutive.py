from typing import List


def main():
    args = [1, 2, 3, 5]
    solution = Solution()
    result = solution.isConsecutive(args)
    print(result)


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        current = nums[0]

        for i in range(1, len(nums)):
            current += 1
            if current != nums[i]:
                return False

        return True


if __name__ == '__main__':
    main()
