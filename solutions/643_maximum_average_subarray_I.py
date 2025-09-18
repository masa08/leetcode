from typing import List


def main():
    solution = Solution()

    # テストケース1: 基本的なケース
    nums1 = [1, 12, -5, -6, 50, 3]
    k1 = 4
    assert abs(solution.findMaxAverage(nums1, k1) - 12.75) < 0.00001

    # テストケース2: 単一要素
    nums2 = [5]
    k2 = 1
    assert solution.findMaxAverage(nums2, k2) == 5.0

    # テストケース3: 全要素が同じ長さ
    nums3 = [0, 1, 1, 3, 3]
    k3 = 4
    assert solution.findMaxAverage(nums3, k3) == 2.0

    print("All tests passed!")


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = max_sum = 0
        for i in range(k):
            cur_sum += nums[i]
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum -= nums[i-k]
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)

        return max_sum/k


if __name__ == '__main__':
    main()
