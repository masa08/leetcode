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
        seen = {}  # { value: index }

        # Traverse the array and store elements in a map
        for index, num in enumerate(nums):
            remain = target - num
            # if remain exists in a map, return indexs
            if remain in seen:
                return [seen[remain], index]
            # if not, store a index and continue
            seen[num] = index

        # blute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i, j]


if __name__ == "__main__":
    main()
