from typing import List


def main():
    args = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    result = solution.removeDuplicates(args)
    print(result)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # seen = {}
        # k = 0

        # for i in range(len(nums)):
        #     if nums[i] not in seen:
        #         nums[k] = nums[i]
        #         k += 1
        #         seen[nums[i]] = 1

        # return k

        k = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == '__main__':
    main()
