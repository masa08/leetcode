from typing import List


def main():
    args = [0, 1, 0, 3, 12]
    solution = Solution()
    result = solution.moveZeroes(args)
    print(result)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0  # To keep position to insert non 0 number
        for fast in range(len(nums)):
            if nums[fast] == 0:
                continue
            if fast != slow:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

        # for num in nums:
        #     if num == 0:
        #         nums.remove(0)
        #         nums.append(0)

        print(nums)


if __name__ == '__main__':
    main()
