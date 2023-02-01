from typing import List


def main():
    args = [3, 2, 2, 3]
    args2 = 3
    solution = Solution()
    result = solution.removeElement(args, args2)
    print(result)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_position = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert_position] = nums[i]
                insert_position += 1

        return insert_position


if __name__ == '__main__':
    main()
