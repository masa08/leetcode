from typing import List


def main():
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    result = solution.twoSum(nums, target)

    print(result)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # { value: index }

        for index, num in enumerate(nums):
            remain = target - num
            if remain in seen:
                return [seen[remain], index]
            seen[num] = index


if __name__ == "__main__":
    main()
