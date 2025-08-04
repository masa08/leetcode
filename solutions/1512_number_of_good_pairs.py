from typing import List


def main():
    solution = Solution()
    result = solution.numIdenticalPairs([1, 2, 3, 1, 1, 3])
    print(f"result: {result}")
    print(result)


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if nums[i] == nums[j]:
                        result += 1

        return result


if __name__ == '__main__':
    main()
