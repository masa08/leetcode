from functools import cmp_to_key
from typing import List


print("=" * 50)
print("Pythonのカスタムソート完全ガイド")
print("=" * 50)

# ============================================
# 1. 基本的なソート（key関数で十分）
# ============================================
print("\n【1. 基本的なソート】")

# 降順
nums = [3, 1, 2, 5, 4]
nums.sort(reverse=True)
print(f"降順: {nums}")

# 絶対値でソート
nums = [-4, -1, 2, 3]
nums.sort(key=abs)
print(f"絶対値: {nums}")

# 複数キー（タプルの自動比較）
students = [("Bob", 90), ("Alice", 85), ("Charlie", 90)]
students.sort(key=lambda x: (-x[1], x[0]))  # 成績降順→名前昇順
print(f"複数キー: {students}")

# ============================================
# 2. よく使うパターン
# ============================================
print("\n【2. よく使うパターン】")

# 偶数を前に、奇数を後に
nums = [5, 2, 8, 1, 9, 4]
nums.sort(key=lambda x: (x % 2, x))
print(f"偶数優先: {nums}")

# カスタム優先順位
priority = {"high": 0, "mid": 1, "low": 2}
tasks = ["low", "high", "mid", "high"]
tasks.sort(key=lambda x: priority[x])
print(f"優先順位: {tasks}")

# 文字列の長さでソート
words = ["apple", "pie", "banana", "cat"]
words.sort(key=len)
print(f"文字列長: {words}")

# ============================================
# 3. cmp_to_keyが真に必要な場合
# ============================================
print("\n【3. cmp_to_keyが必要な例：2要素の関係性で判断】")

# LeetCode 179: Largest Number
# 「2つの数を連結した結果」で比較する必要がある


def largest_number(nums):
    """
    [3, 30, 34, 5, 9] → "9534330"

    なぜcmp_to_keyが必要？
    - 3と30を比較する時、"330" vs "303"を比較したい
    - これは単純な変換では表現できない（2要素の関係性）
    """
    def compare(x, y):
        # xとyを連結して比較
        if x + y > y + x:
            return -1  # xを前に
        elif x + y < y + x:
            return 1   # yを前に
        else:
            return 0

    str_nums = [str(n) for n in nums]
    str_nums.sort(key=cmp_to_key(compare))

    result = ''.join(str_nums)
    # 全て0の場合の処理
    return '0' if result[0] == '0' else result


print(f"入力: [3,30,34,5,9]")
print(f"出力: {largest_number([3,30,34,5,9])}")

# ============================================
# まとめ
# ============================================
print("\n" + "=" * 50)
print("【まとめ】")
print("90%のケース: key関数で十分")
print("  - 単純な変換: key=abs, key=len")
print("  - 複数条件: key=lambda x: (条件1, 条件2)")
print("  - 降順: reverse=True または key=lambda x: -x")
print()
print("10%のケース: cmp_to_key")
print("  - 2要素の「関係性」で判断が必要な時")
print("  - 例: 連結結果の比較、カスタム順序関係")
print("=" * 50)
