# 区間 (Intervals)

区間の重複、統合、スケジューリングなどを扱う問題のパターンです。

## 基本概念

### 区間の表現

- `[start, end]` または `(start, end)`
- 閉区間 vs 開区間の違いに注意
- 通常は `[start, end)` で半開区間を使用

### 区間の関係

1. **重複**: `max(start1, start2) < min(end1, end2)`
2. **隣接**: `end1 == start2` または `end2 == start1`
3. **包含**: 一方が他方を完全に含む
4. **分離**: 重複も隣接もしない

## 重要なパターン

### 1. 区間の統合 (Merge Intervals)

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # 開始時間でソート
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # 重複あり
            merged[-1] = [last[0], max(last[1], current[1])]
        else:  # 重複なし
            merged.append(current)
    
    return merged
```

### 2. 区間の挿入 (Insert Interval)

- ソート済み区間リストに新しい区間を挿入
- 前後の区間との統合を考慮

### 3. 非重複区間の最大数

```python
def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])  # 終了時間でソート
    count = 1
    last_end = intervals[0][1]
    
    for start, end in intervals[1:]:
        if start >= last_end:  # 重複なし
            count += 1
            last_end = end
    
    return count
```

### 4. 最小会議室数

- 同時進行する区間の最大数
- ヒープまたはスイープラインアルゴリズム

### 5. 区間の削除

- 重複する区間を最小数削除
- 矢で風船を割る問題

## アルゴリズムテクニック

### 1. ソート戦略

- **開始時間でソート**: 統合、挿入問題
- **終了時間でソート**: スケジューリング問題
- **長さでソート**: 特定の最適化問題

### 2. スイープライン

```python
def sweep_line(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))   # 開始イベント
        events.append((end, -1))    # 終了イベント
    
    events.sort()
    active = 0
    max_active = 0
    
    for time, delta in events:
        active += delta
        max_active = max(max_active, active)
    
    return max_active
```

### 3. 線分木 (Segment Tree)

- 区間クエリの効率的な処理
- 区間更新、区間最大値など

## 実装のポイント

1. **エッジケース**: 空リスト、単一区間
2. **境界条件**: 区間の端点での重複判定
3. **ソートの安定性**: 同じキーの要素の順序
4. **時間の表現**: 整数 vs 実数

## 典型的な問題

-  Merge Intervals
-  Insert Interval
-  Meeting Rooms
-  Meeting Rooms II
-  Non-overlapping Intervals
-  Minimum Number of Arrows to Burst Balloons
-  Teemo Attacking
-  Add Bold Tag in String
-  My Calendar I
-  My Calendar II
-  My Calendar III
-  Interval List Intersections
-  Meeting Scheduler
