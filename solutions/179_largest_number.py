"""
179. Largest Number

なぜcmp_to_keyが必要か：
- key関数は引数を1つしか持てない（要素を独立して評価）
- この問題では2つの要素を連結して比較する必要がある（相手次第で優先度が変わる）
  例: 3は30に対しては前（"330" > "303"）、34に対しては後ろ（"343" > "334"）
- 隣り合う要素の関係性で判断が必要な場合はcmp_to_keyを使う

処理の流れ（[3,30,34,5,9]の例）：
1. 各ペアで連結結果を比較
   - 9 vs 5: "95" > "59" → 9が前
   - 5 vs 34: "534" > "345" → 5が前
   - 34 vs 3: "343" > "334" → 34が前
   - 3 vs 30: "330" > "303" → 3が前
2. 結果: [9,5,34,3,30] → "9534330"
"""
from functools import cmp_to_key
from typing import List


def main():
    solution = Solution()

    # テストケース1: 基本
    nums1 = [10, 2]
    print(f"Input: {nums1} → Output: {solution.largestNumber(nums1)}")

    # テストケース2: 例題
    nums2 = [3, 30, 34, 5, 9]
    print(f"Input: {nums2} → Output: {solution.largestNumber(nums2)}")

    # テストケース3: 全て0
    nums3 = [0, 0]
    print(f"Input: {nums3} → Output: {solution.largestNumber(nums3)}")


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return -1 if x + y > y + x else 1

        str_nums = [str(n) for n in nums]
        largest_num = "".join(sorted(str_nums, key=cmp_to_key(compare)))

        return "0" if largest_num[0] == "0" else largest_num


if __name__ == '__main__':
    main()
