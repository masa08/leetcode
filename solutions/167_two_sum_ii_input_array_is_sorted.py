from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert solution.twoSum([2, 3, 4], 6) == [1, 3]
    assert solution.twoSum([-1, 0], -1) == [1, 2]

    # エッジケース
    assert solution.twoSum([1, 2], 3) == [1, 2]  # 最小サイズ
    assert solution.twoSum([0, 0, 3, 4], 0) == [1, 2]  # 重複値
    assert solution.twoSum([-3, -1, 0, 2, 5], -1) == [1, 4]  # 負の数含む

    print("All tests passed!")


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if target == total:
                return [left+1, right+1]
            elif target < total:
                right -= 1
            else:
                left += 1

        return [-1, -1]


if __name__ == '__main__':
    main()
