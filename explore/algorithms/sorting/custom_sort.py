from functools import cmp_to_key
from typing import List


print("=" * 50)
print("Pythonのカスタムソート基礎")
print("=" * 50)

# 1. key関数の基本
print("\n1. key関数を使う（推奨）")
versions = ["10.1.0", "1.1.0", "0.1.1"]

# バージョン番号を数値のリストに変換してソート
versions.sort(key=lambda v: [int(x) for x in v.split('.')])
print(f"バージョンソート: {versions}")

# 2. 複数キーでソート
print("\n2. 複数キーでソート")

# タプルがどう比較されるか実験
print("【重要】Pythonのタプル比較の仕組み:")
print("タプルは自動的に左から順に比較される！")
print()

# 実験1: タプルの比較
print("実験1: タプル同士の比較")
print(f"  (1, 5) < (2, 3) = {(1, 5) < (2, 3)}")  # True (最初の要素1 < 2で決まる)
print(f"  (2, 5) < (2, 3) = {(2, 5) < (2, 3)}")  # False (最初が同じなので、5 < 3で判定)
print()

# 実験2: 3要素のタプル
print("実験2: 3要素のタプル")
print(f"  (1, 2, 3) < (1, 2, 4) = {(1, 2, 3) < (1, 2, 4)}")  # True
print("  → 最初の2つが同じなので、3番目で決まる")
print()

# 実際の例
print("実際の例で理解しよう:")
students = [("Bob", 90), ("Alice", 85), ("Charlie", 90)]
print(f"元のデータ: {students}")
print()

print("key関数で変換後のタプル:")
transformed = []
for student in students:
    new_tuple = (-student[1], student[0])
    transformed.append(new_tuple)
    print(f"  {student} → {new_tuple}")

print("\nPythonがこれらのタプルを比較:")
print(f"  (-90, 'Bob') vs (-85, 'Alice')")
print(f"    → 最初の要素: -90 < -85 なので (-90, 'Bob')が前")
print(f"  (-90, 'Alice') vs (-90, 'Bob')")  
print(f"    → 最初の要素: -90 = -90 なので2番目を見る")
print(f"    → 2番目の要素: 'Alice' < 'Bob' なので (-90, 'Alice')が前")

# 成績で降順、同じなら名前で昇順
students.sort(key=lambda x: (-x[1], x[0]))
print(f"\nソート結果: {students}")

# 3. cmp_to_key（2つの要素を比較）
print("\n3. cmp_to_key（複雑な比較が必要な時）")

print("【重要】cmp_to_keyの仕組み:")
print("比較関数は2つの要素を受け取り、どちらが前に来るべきかを返す")
print("  戻り値: -1 (左が前), 0 (同じ), 1 (右が前)")
print()

# 簡単な例で理解
print("簡単な例: 数値の降順ソート")
def compare_desc(a, b):
    print(f"  比較: {a} と {b}")
    if a > b:
        print(f"    {a} > {b} なので {a} を前に → 戻り値: -1")
        return -1
    elif a < b:
        print(f"    {a} < {b} なので {b} を前に → 戻り値: 1") 
        return 1
    else:
        print(f"    {a} = {b} なので同じ → 戻り値: 0")
        return 0

nums = [3, 1, 2]
print(f"元のデータ: {nums}")
nums.sort(key=cmp_to_key(compare_desc))
print(f"降順ソート結果: {nums}")
print()

# 複雑な例: バージョン比較
print("複雑な例: バージョン比較")
def compare_version(v1, v2):
    """2つのバージョンを比較"""
    print(f"  比較: {v1} と {v2}")
    
    a = [int(x) for x in v1.split('.')]
    b = [int(x) for x in v2.split('.')]
    
    print(f"    {v1} → {a}")
    print(f"    {v2} → {b}")

    if a < b:
        print(f"    {a} < {b} なので {v1} を前に → 戻り値: -1")
        return -1
    elif a > b:
        print(f"    {a} > {b} なので {v2} を前に → 戻り値: 1")
        return 1
    else:
        print(f"    {a} = {b} なので同じ → 戻り値: 0")
        return 0

versions = ["10.1.0", "1.1.0", "0.1.1"]
print(f"元のデータ: {versions}")
versions.sort(key=cmp_to_key(compare_version))
print(f"バージョンソート結果: {versions}")
print()

print("key関数 vs cmp_to_key:")
print("  key関数:     各要素を変換して比較（推奨、高速）")
print("  cmp_to_key:  2要素を直接比較（複雑な比較ロジックが必要な時）")

# 4. よく使うパターン
print("\n4. よく使うパターン")

# 偶数を前に、奇数を後に
nums = [5, 2, 8, 1, 9, 4]
nums.sort(key=lambda x: (x % 2, x))
print(f"偶数優先: {nums}")

# カスタム優先順位
priority = {"high": 0, "mid": 1, "low": 2}
tasks = ["low", "high", "mid", "high"]
tasks.sort(key=lambda x: priority[x])
print(f"優先順位: {tasks}")

# 5. LeetCode頻出例: Largest Number (179)
print("\n5. LeetCode例: 最大数を作る")


def largest_number(nums):
    # 連結時に大きくなる順に並べる
    def compare(x, y):
        if x + y > y + x:
            return -1  # xを前に
        elif x + y < y + x:
            return 1  # yを前に
        else:
            return 0

    str_nums = [str(n) for n in nums]
    str_nums.sort(key=cmp_to_key(compare))

    result = ''.join(str_nums)
    return '0' if result[0] == '0' else result


print(f"[3,30,34,5,9] -> {largest_number([3,30,34,5,9])}")

print("\n" + "=" * 50)
print("ポイント:")
print("- key関数: 各要素を比較可能な値に変換（シンプル、高速）")
print("- cmp_to_key: 2要素の複雑な比較が必要な時に使用")
print("- タプルは自動的に辞書順で比較される")
print("=" * 50)
