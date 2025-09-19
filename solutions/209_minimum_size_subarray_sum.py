from typing import List


def main():
    solution = Solution()

    # 基本ケース: 複数の有効な部分配列
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2  # [4,3]

    # エッジケース: 単一要素で条件を満たす
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1  # [4]

    # エッジケース: 解が存在しない
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0

    # エッジケース: 全体がギリギリ
    assert solution.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5

    print("All tests passed!")


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left = cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target:
                min_len = min(min_len, right-left+1)
                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0


if __name__ == '__main__':
    main()
