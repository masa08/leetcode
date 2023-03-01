from typing import List


def main():
    args = [1, 1, 1, 0, 0]
    solution = Solution()
    result = solution.findMaxConsecutiveOnes(args)
    print(result)


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = temp = 0 if nums[0] == 0 else 1

        for i in range(1, len(nums)):
            if nums[i] == 0:
                temp = 0
                continue

            if nums[i-1] == nums[i]:
                temp += 1
            else:
                temp = 1

            maximum = max(maximum, temp)

        return maximum


if __name__ == '__main__':
    main()
