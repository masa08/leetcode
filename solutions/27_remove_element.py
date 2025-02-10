from typing import List


def main():
    args = [3, 2, 2, 3]
    args2 = 3
    solution = Solution()
    result = solution.removeElement(args, args2)
    print(result)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if val != nums[i]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == '__main__':
    main()
