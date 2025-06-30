# 二分探索 (Binary Search)

ソート済みデータに対する効率的な探索アルゴリズムです。

## 基本概念

### 二分探索の原理

- ソート済み配列で中央値と比較
- 探索範囲を半分ずつ絞り込み
- 時間計算量: O(log n)

### 基本テンプレート

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

## 重要なバリエーション

### 1. Lower Bound（左端探索）

```python
# target以上の最小インデックス
left, right = 0, len(nums)
while left < right:
    mid = (left + right) // 2
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid
```

### 2. Upper Bound（右端探索）

```python
# targetより大きい最小インデックス
left, right = 0, len(nums)
while left < right:
    mid = (left + right) // 2
    if nums[mid] <= target:
        left = mid + 1
    else:
        right = mid
```

### 3. 回転配列での探索

- 配列が部分的にソートされている
- どちら半分がソート済みかを判定

### 4. 答えで二分探索

- 最小/最大値を求める問題
- 判定関数を使って可能性を二分探索

## 応用パターン

### 1. Peak Finding

- 山の頂上を見つける
- 局所最大値の探索

### 2. Search in 2D Matrix

- 行と列がソートされた2D配列
- 右上角または左下角からスタート

### 3. 最小値の最大化/最大値の最小化

- Capacity To Ship Packages問題
- Split Array Largest Sum問題

## 注意点

- **境界条件**: `left <= right` vs `left < right`
- **オーバーフロー対策**: `mid = left + (right - left) // 2`
- **無限ループ回避**: 更新式の正確性

## 典型的な問題

-  Search in Rotated Sorted Array
-  Find First and Last Position of Element
-  Search Insert Position
-  Sqrt(x)
-  Search a 2D Matrix
-  Find Minimum in Rotated Sorted Array
-  Find Peak Element
-  First Bad Version
-  Guess Number Higher or Lower
-  Split Array Largest Sum
-  Koko Eating Bananas
-  Capacity To Ship Packages Within D Days
