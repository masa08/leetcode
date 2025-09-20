import heapq
import random
from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    # エッジケース
    assert solution.findKthLargest([1], 1) == 1
    assert solution.findKthLargest([1, 2], 1) == 2
    assert solution.findKthLargest([1, 2], 2) == 1

    print("All tests passed!")


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # QuickSelect - O(n) average, O(n²) worst
        def partition(nums: List[int], low: int, high: int):
            # ランダムpivotを選択（最悪ケースO(n²)を回避）
            pivot_index = random.randint(low, high)
            pivot_value = nums[pivot_index]

            # pivotを配列の最後に移動（処理を簡単にするため）
            nums[pivot_index], nums[high] = nums[high], nums[pivot_index]

            # iは「pivot未満」領域の境界を追跡
            i = low

            # 各要素をpivotと比較して配置
            for j in range(low, high):
                if nums[j] < pivot_value:
                    # pivot未満の要素を左側に移動
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1  # 境界を右に移動

            # pivotを正しい位置（境界）に配置
            nums[i], nums[high] = nums[high], nums[i]
            return i  # pivotの最終位置を返す

        def quickselect(nums: List[int], low: int, high: int, k: int):
            # ベースケース：要素が1つの場合
            if low == high:
                return nums[low]

            # 配列を分割し、pivot位置を取得
            pivot = partition(nums, low, high)

            # 目標位置との比較
            if pivot == k:
                return nums[pivot]  # 発見！
            elif pivot > k:
                # 目標は左側にある
                return quickselect(nums, low, pivot - 1, k)
            else:
                # 目標は右側にある
                return quickselect(nums, pivot + 1, high, k)

        # k番目に大きい = (n-k)番目に小さい（0-indexed）
        return quickselect(nums, 0, len(nums) - 1, len(nums) - k)

        # Min Heap - O(n log k) 安定した性能
        # サイズkのmin heapを維持、常にk個の最大値を保持
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)  # 要素を追加
        #     if len(heap) > k:
        #         heapq.heappop(heap)     # 最小値を削除（k個に制限）
        # return heap[0]  # heap[0]がk番目に大きい値

        # Max Heap - O(n + k log n) ヒープ化が高速
        # 全要素を負数にしてmax heapを実現（Pythonはmin heapのみ）
        # nums = [-1 * num for num in nums]  # 符号反転
        # heapq.heapify(nums)                # O(n)でヒープ化
        # for _ in range(k-1):
        #     heapq.heappop(nums)            # 最大値をk-1回削除
        # return heapq.heappop(nums) * -1    # k番目最大値を復元


if __name__ == '__main__':
    main()
