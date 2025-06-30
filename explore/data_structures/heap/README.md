# ヒープ (Heap)

ヒープは完全二分木の性質を満たす特殊な木構造で、優先度付きキューの実装に使われます。

## 基本概念

### ヒープの性質

1. **完全二分木**: 最下段以外は全て埋まり、最下段は左から順に埋まる
2. **ヒープ条件**:
   - **最大ヒープ**: 親ノード ≥ 子ノード
   - **最小ヒープ**: 親ノード ≤ 子ノード

### 配列での表現

- 親ノード: `i`
- 左の子: `2*i + 1`
- 右の子: `2*i + 2`
- 親: `(i-1) // 2`

## 主な操作

### 1. 挿入 (Insert) - O(log n)

1. 最後尾に要素を追加
2. ヒープ条件を満たすまで上方向に交換（heapify up）

### 2. 削除 (Extract) - O(log n)

1. ルート要素を取得
2. 最後尾の要素をルートに移動
3. ヒープ条件を満たすまで下方向に交換（heapify down）

### 3. ヒープ構築 (Build Heap) - O(n)

- 配列から効率的にヒープを構築

## 応用

### 1. 優先度付きキュー

- タスクスケジューリング
- イベント処理

### 2. ヒープソート

- O(n log n)の安定したソート

### 3. Top K問題

- K個の最大/最小要素を効率的に管理

## Pythonでの使用

```python
import heapq

# 最小ヒープ（デフォルト）
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 4)

# 最小値を取得
min_val = heapq.heappop(heap)  # 1

# 最大ヒープの実現（値を負にする）
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -4)
max_val = -heapq.heappop(max_heap)  # 4
```

## ファイル構成

- `example.py`: ヒープの基本実装
- `heap_sort.py`: ヒープソートの実装

## 典型的な問題

-  Kth Largest Element in an Array
-  Top K Frequent Elements
-  Merge k Sorted Lists
-  Find Median from Data Stream
-  Kth Largest Element in a Stream
