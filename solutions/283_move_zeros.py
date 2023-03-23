from typing import List


def main():
    args = [0, 1, 0, 3, 12]
    solution = Solution()
    result = solution.moveZeroes(args)
    print(result)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        targetIndex = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                continue
            nums[index], nums[targetIndex] = nums[targetIndex], nums[index]
            targetIndex += 1

        # for num in nums:
        #     if num == 0:
        #         nums.remove(0)
        #         nums.append(0)

        print(nums)


if __name__ == '__main__':
    main()
