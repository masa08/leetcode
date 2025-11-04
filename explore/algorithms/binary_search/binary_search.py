"""
Binary Search - Complete Implementation

3つのパターン:
1. Basic Search - 値がユニーク
2. Lower Bound - 最初の出現（最頻出）
3. Upper Bound - 最後の出現
"""

from typing import List


# ============================================================
# Pattern 1: Basic Search (値がユニーク)
# ============================================================

def binary_search(nums: List[int], target: int) -> int:
    """
    基本的な二分探索

    Time: O(log N), Space: O(1)
    使用条件: 値がユニーク
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ============================================================
# Pattern 2: Lower Bound (最初の出現) - 最重要！
# ============================================================

def lower_bound(nums: List[int], target: int) -> int:
    """
    Lower Bound: nums[i] >= target となる最小のインデックス

    視覚化:
        nums = [1,3,3,4,4,4,4,4,19], target = 4
        cond:   F F F T T T T T  T  (nums[i] >= 4)
                |-ng| |---ok-----|
                      ↑ index 3 (最初の4)

    Time: O(log N), Space: O(1)
    """
    N = len(nums)

    # エッジケース: 範囲外
    if not (nums[0] <= target <= nums[N - 1]):
        return -1

    # エッジケース: nums[0] == targetだとngを初期化できない
    if nums[0] == target:
        return 0

    # 境界探索
    ok, ng = N - 1, 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if nums[mid] >= target:  # 条件: >=
            ok = mid
        else:
            ng = mid

    return ok if nums[ok] == target else -1


# ============================================================
# Pattern 3: Upper Bound (最後の出現)
# ============================================================

def upper_bound(nums: List[int], target: int) -> int:
    """
    Upper Bound: nums[i] <= target となる最大のインデックス

    視覚化:
        nums = [1,3,3,4,4,4,4,4,19], target = 4
        cond:   T T T T T T T T  F  (nums[i] <= 4)
                |---ok-------| |ng|
                              ↑ index 7 (最後の4)

    Time: O(log N), Space: O(1)
    """
    N = len(nums)

    # エッジケース: 範囲外
    if not (nums[0] <= target <= nums[N - 1]):
        return -1

    # エッジケース: nums[-1] == targetだとngを初期化できない
    if nums[N - 1] == target:
        return N - 1

    # 境界探索（okとngが逆）
    ok, ng = 0, N - 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if nums[mid] <= target:  # 条件: <=
            ok = mid
        else:
            ng = mid

    return ok if nums[ok] == target else -1


# ============================================================
# 応用: Find Range (LeetCode 34)
# ============================================================

def find_range(nums: List[int], target: int) -> List[int]:
    """
    最初と最後の出現位置を返す

    Example:
        nums = [1,3,3,4,4,4,4,4,19], target = 4
        return [3, 7]
    """
    start = lower_bound(nums, target)
    if start == -1:
        return [-1, -1]

    end = upper_bound(nums, target)
    return [start, end]


# ============================================================
# Tests
# ============================================================

def test_basic_search():
    nums = [1, 3, 4, 19, 20, 33, 53]
    assert binary_search(nums, 4) == 2
    assert binary_search(nums, 22) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([], 1) == -1
    print("✓ Basic search tests passed")


def test_lower_bound():
    nums = [1, 3, 3, 4, 4, 4, 4, 4, 19]

    # 基本
    assert lower_bound(nums, 4) == 3  # 最初の4
    assert lower_bound(nums, 3) == 1  # 最初の3

    # 存在しない
    assert lower_bound(nums, 5) == -1
    assert lower_bound(nums, 0) == -1

    # エッジ
    assert lower_bound(nums, 1) == 0
    assert lower_bound(nums, 19) == 8

    print("✓ Lower bound tests passed")


def test_upper_bound():
    nums = [1, 3, 3, 4, 4, 4, 4, 4, 19]

    # 基本
    assert upper_bound(nums, 4) == 7  # 最後の4
    assert upper_bound(nums, 3) == 2  # 最後の3

    # 存在しない
    assert upper_bound(nums, 5) == -1
    assert upper_bound(nums, 0) == -1

    # エッジ
    assert upper_bound(nums, 1) == 0
    assert upper_bound(nums, 19) == 8

    print("✓ Upper bound tests passed")


def test_find_range():
    nums = [1, 3, 3, 4, 4, 4, 4, 4, 19]

    assert find_range(nums, 4) == [3, 7]
    assert find_range(nums, 3) == [1, 2]
    assert find_range(nums, 5) == [-1, -1]

    print("✓ Find range tests passed")


def main():
    """全テストを実行"""
    test_basic_search()
    test_lower_bound()
    test_upper_bound()
    test_find_range()
    print("\n🎉 All tests passed!")

    # 使い方の例
    print("\n" + "="*50)
    print("使用例:")
    print("="*50)

    nums = [1, 3, 3, 4, 4, 4, 4, 4, 19]
    target = 4

    print(f"nums = {nums}")
    print(f"target = {target}\n")

    print(f"Lower bound (最初の{target}): index {lower_bound(nums, target)}")
    print(f"Upper bound (最後の{target}): index {upper_bound(nums, target)}")
    print(f"Range: {find_range(nums, target)}")


if __name__ == "__main__":
    main()
