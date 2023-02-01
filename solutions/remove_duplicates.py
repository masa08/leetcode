from typing import List


def main():
    args = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    result = solution.removeDuplicates(args)
    print(result)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        insert_position = 0

        for i in range(0, len(nums)):
            val = nums[i]

            if val in seen:
                seen[val] += 1
            else:
                seen[val] = 1
                nums[insert_position] = val
                insert_position += 1

        return insert_position


if __name__ == '__main__':
    main()
