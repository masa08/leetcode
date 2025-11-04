# 二分探索（Binary Search）

## 核心概念

二分探索の本質は**「条件がTrue/Falseに変わる境界を見つける」**こと。

```text
配列: [1, 3, 3, 4, 4, 4, 4, 4, 19]
条件: nums[i] >= 4
      F  F  F  T  T  T  T  T  T
      |-ng-| |-----ok-----|
             ↑
        この境界を見つける
```

## 3つのパターン

| パターン | 条件 | 初期化 | 用途 |
|---------|------|--------|------|
| Basic | `== target` | `left=0, right=N-1` | 値がユニーク |
| Lower Bound | `>= target` | `ok=N-1, ng=0` | 最初の出現 |
| Upper Bound | `<= target` | `ok=0, ng=N-1` | 最後の出現 |

### 視覚化

```text
nums = [1,3,3,4,4,4,4,4,19], target = 4

Lower Bound (>=):
    F F F T T T T T T  → index 3 (最初の4)
    |-ng| |---ok----|

Upper Bound (<=):
    T T T T T T T T F  → index 7 (最後の4)
    |---ok------| |ng|
```

## 実装

### Pattern 1: Basic Search

```python
def binary_search(nums, target):
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
```

### Pattern 2: Lower Bound（最頻出）

```python
def lower_bound(nums, target):
    N = len(nums)

    # エッジケース
    if not (nums[0] <= target <= nums[N-1]):
        return -1
    if nums[0] == target:
        return 0

    # ok/ngパターン
    ok, ng = N - 1, 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if nums[mid] >= target:  # >=
            ok = mid
        else:
            ng = mid

    return ok if nums[ok] == target else -1
```

### Pattern 3: Upper Bound

```python
def upper_bound(nums, target):
    N = len(nums)

    # エッジケース
    if not (nums[0] <= target <= nums[N-1]):
        return -1
    if nums[N-1] == target:
        return N - 1

    # ok/ngパターン（逆向き）
    ok, ng = 0, N - 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if nums[mid] <= target:  # <=
            ok = mid
        else:
            ng = mid

    return ok if nums[ok] == target else -1
```

## OK/NGパターンの理解

### 4つのステップ

1. **条件を定義**: 「最初の4」 → `nums[i] >= 4`
2. **可視化**: `F F F T T T T T T` → どこが境界？
3. **ok/ng初期化**: ok=絶対True, ng=絶対False
4. **実装**: `while abs(ok - ng) > 1:`

### なぜok/ngを使う？

- ✅ **重複値に対応**できる
- ✅ **境界を確実**に見つけられる
- ✅ `left/right`より直感的

### ok/ngの初期化ルール

```python
# Lower Bound: 最初のTrue を探す
# 条件: nums[i] >= target
# F F F T T T
# |ng| |-ok-|
ok, ng = N-1, 0  # nums[-1]は絶対>=, nums[0]は可能性あり

# Upper Bound: 最後のTrue を探す
# 条件: nums[i] <= target
# T T T T F F
# |-ok-| |ng|
ok, ng = 0, N-1  # nums[0]は絶対<=, nums[-1]は可能性あり
```

## よくあるバグ

| バグ | ❌ Wrong | ✅ Fix |
|------|----------|--------|
| 無限ループ | `while ok < ng:` | `while abs(ok - ng) > 1:` |
| 条件ミス | `nums[mid] > target` | `nums[mid] >= target` (Lower) |
| エッジケース | 範囲チェックなし | `if not (nums[0] <= target <= nums[-1])` |
| 最終チェック忘れ | `return ok` | `return ok if nums[ok] == target else -1` |

## チェックリスト

実装時に必ず確認:

- [ ] 条件は正しい？（`>=`, `<=`, `==`）
- [ ] ok/ng正しく初期化？
- [ ] エッジケース処理（範囲外、境界値）
- [ ] `abs(ok - ng) > 1` 使用？
- [ ] 最後に `nums[ok] == target` チェック？

## 練習問題

### 基礎（値の探索）

- [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

### 境界の探索

- [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)
- [34. Find First and Last Position](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) ⭐ 最重要

### Lower/Upper Bound

- [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
- [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
- [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

## ファイル構成

```text
binary_search/
├── README.md              # このファイル
├── binary_search.py       # 全実装（テスト付き）
└── visual_patterns.py  # 視覚的デモ（学習用）
```

### 使い方

```bash
# 実装とテストを確認
python binary_search.py

# 視覚的デモを見る
python visual_patterns.py
```

## 学習の流れ

1. この README を読む（10分）
2. `python visual_patterns.py` で視覚的に理解（5分）
3. `binary_search.py` のコードを読む（15分）
4. LeetCode 34 を解く（30分）

## 実践での使い分け

```python
if 値がユニーク:
    binary_search()  # Basic
elif 重複あり and 最初を探す:
    lower_bound()    # 最頻出
elif 重複あり and 最後を探す:
    upper_bound()
else:
    迷ったら lower_bound()  # 最も汎用的
```

## Python bisect

標準ライブラリも利用可能（面接では自分で実装推奨）:

```python
from bisect import bisect_left, bisect_right

nums = [1, 3, 3, 4, 4, 4, 4, 4, 19]

bisect_left(nums, 4)   # 3 (Lower Bound)
bisect_right(nums, 4)  # 8 (Upper Bound + 1) ⚠️ 注意
```

---

**計算量**: `O(log N)` - 要素数Nに対して毎回半分ずつ絞り込む
