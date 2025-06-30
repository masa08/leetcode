# キュー (Queue)

キューはFIFO（First In First Out）の原則に従うデータ構造です。

## 基本概念

### キューの特性

- **FIFO**: 最初に入れた要素が最初に出る
- **主な操作**: enqueue（追加）とdequeue（取り出し）

### 実装方法

1. **配列ベース**: 循環バッファを使用
2. **連結リストベース**: 挿入・削除がO(1)
3. **Pythonのcollections.deque**: 効率的な実装

## 主な操作

### 1. Enqueue（追加）- O(1)

- 要素を末尾に追加

### 2. Dequeue（取り出し）- O(1)

- 先頭の要素を取り出して削除

### 3. Peek/Front - O(1)

- 先頭の要素を参照（削除しない）

### 4. IsEmpty - O(1)

- キューが空かどうかを確認

## Pythonでの実装

### collections.dequeを使用（推奨）

```python
from collections import deque

queue = deque()
queue.append(1)      # enqueue
queue.append(2)
item = queue.popleft()  # dequeue, returns 1
```

### リストを使用（非効率）

```python
queue = []
queue.append(1)      # enqueue - O(1)
item = queue.pop(0)  # dequeue - O(n) ⚠️非効率
```

## キューの種類

### 1. 単純キュー

- 基本的なFIFO操作

### 2. 循環キュー

- 固定サイズで効率的なメモリ使用

### 3. 優先度付きキュー

- 要素に優先度があり、高優先度から取り出す
- ヒープで実装

### 4. 双端キュー（Deque）

- 両端から挿入・削除可能

## 応用

### 1. 幅優先探索（BFS）

- グラフやツリーの探索

### 2. タスクスケジューリング

- プロセス管理、印刷ジョブ

### 3. キャッシュ実装

- LRUキャッシュの一部として

### 4. レベル順走査

- ツリーのレベル順処理

## ファイル構成

- `base.py`: キューの基本実装

## 典型的な問題

- 102. Binary Tree Level Order Traversal
- 225. Implement Stack using Queues
- 622. Design Circular Queue
- 239. Sliding Window Maximum
- 346. Moving Average from Data Stream
