from typing import List


def main():
    solution = Solution()

    # 基本ケース - 重複あり
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    assert solution.containsDuplicate([1, 1, 2, 3]) == True

    # 基本ケース - 重複なし
    assert solution.containsDuplicate([1, 2, 3, 4]) == False

    # エッジケース
    assert solution.containsDuplicate([1]) == False
    assert solution.containsDuplicate([]) == False

    print("All tests passed!")


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for num in nums:
            if num in mapping:
                return True
            else:
                mapping[num] = 1

        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False


if __name__ == '__main__':
    main()
