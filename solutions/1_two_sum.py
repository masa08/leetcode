from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]

    # エッジケース
    assert solution.twoSum([0, 4, 3, 0], 0) == [0, 3]
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # 大きい数値
    assert solution.twoSum([1000000000, 999999999, 1, 2], 1000000001) == [0, 2]

    print("All tests passed!")


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: Hash Map (One-pass)

        1. Traverse the array once
        2. For each element, check if (target - num) exists in the map
        3. If found, return the indices; otherwise store current element

        Time: O(n) - single pass through the array
        Space: O(n) - hash map to store elements

        Trade-off: Optimal solution using hash map for O(1) lookup
        """
        seen = {}  # { value: index }

        for index, num in enumerate(nums):
            remain = target - num
            if remain in seen:
                return [seen[remain], index]
            seen[num] = index

        # Brute Force Alternative:
        # Time: O(n²) - nested loops
        # Space: O(1) - no extra space
        #
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i, j]


if __name__ == "__main__":
    main()
