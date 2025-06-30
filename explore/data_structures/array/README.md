# 配列 (Array)

要素を連続したメモリ領域に格納するデータ構造です。

## 基本概念

### 配列の特徴
- **固定サイズ**: 作成時にサイズが決定（静的配列）
- **インデックスアクセス**: O(1)で任意の要素にアクセス
- **連続メモリ**: 要素が物理的に隣接して配置

### Python での配列
```python
# リスト（動的配列）
arr = [1, 2, 3, 4, 5]
print(arr[0])  # インデックスアクセス: O(1)

# array モジュール（型指定配列）
import array
int_array = array.array('i', [1, 2, 3, 4, 5])
```

## 基本操作

### 1. アクセス・更新 - O(1)
```python
# 読み取り
value = arr[index]

# 更新
arr[index] = new_value
```

### 2. 挿入 - O(n)
```python
# 末尾に追加: O(1) amortized
arr.append(value)

# 指定位置に挿入: O(n)
arr.insert(index, value)
```

### 3. 削除 - O(n)
```python
# 末尾から削除: O(1)
arr.pop()

# 指定位置から削除: O(n)
arr.pop(index)

# 値で削除: O(n)
arr.remove(value)
```

### 4. 探索 - O(n)
```python
# 線形探索
if value in arr:  # O(n)
    index = arr.index(value)
```

## 多次元配列

### 2次元配列
```python
# リストのリスト
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# NumPy配列（数値計算用）
import numpy as np
np_matrix = np.array([[1, 2, 3], [4, 5, 6]])
```

## 配列の種類

### 1. 静的配列
- サイズが固定
- メモリ効率が良い
- 例：C言語の配列、Python の array モジュール

### 2. 動的配列
- サイズが可変
- 必要に応じて自動拡張
- 例：Python の list、C++ の vector

## メモリレイアウト

### キャッシュ効率
- **局所性**: 隣接要素は物理的に近い
- **プリフェッチ**: CPU が先読みしやすい
- **連続アクセス**: 非常に高速

### vs 連結リスト
| 操作 | 配列 | 連結リスト |
|------|------|------------|
| アクセス | O(1) | O(n) |
| 挿入（末尾） | O(1)* | O(1) |
| 挿入（中間） | O(n) | O(1)** |
| 削除 | O(n) | O(1)** |
| メモリ効率 | 良い | 劣る（ポインタ） |
| キャッシュ | 良い | 劣る |

*amortized、**ノードが既知の場合

## 実装テクニック

### 1. 循環配列
```python
class CircularArray:
    def __init__(self, size):
        self.arr = [None] * size
        self.head = 0
        self.size = size
    
    def get(self, index):
        return self.arr[(self.head + index) % self.size]
```

### 2. 動的拡張
```python
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.arr = [None] * self.capacity
    
    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = value
        self.size += 1
    
    def _resize(self):
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
```

## 応用パターン
- **前缀和**: 範囲クエリの高速化
- **スライディングウィンドウ**: 固定サイズの部分配列処理
- **Two Pointers**: 効率的な探索・操作

## 典型的な問題
- Two Sum
- Remove Duplicates from Sorted Array
- Merge Sorted Array
- Rotate Array
- Product of Array Except Self
- Maximum Subarray
- Container With Most Water
- 3Sum
- Move Zeroes
- Remove Element