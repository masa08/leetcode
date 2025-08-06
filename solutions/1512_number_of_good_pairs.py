from collections import defaultdict
from typing import List


def main():
    solution = Solution()

    # Test case 1
    nums = [1, 2, 3, 1, 1, 3]
    print(solution.numIdenticalPairs(nums))  # Expected: 4

    # Test case 2
    nums = [1, 1, 1, 1]
    print(solution.numIdenticalPairs(nums))  # Expected: 6

    # Test case 3
    nums = [1, 2, 3]
    print(solution.numIdenticalPairs(nums))  # Expected: 0


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # result = 0

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i < j:
        #             if nums[i] == nums[j]:
        #                 result += 1

        # return result

        num_of_good_pairs = 0
        counts = defaultdict(int)

        for i in range(len(nums)):
            counts[nums[i]] += 1

        for count in counts.values():
            num_of_good_pairs += count * (count - 1) // 2

        return num_of_good_pairs


if __name__ == '__main__':
    main()
