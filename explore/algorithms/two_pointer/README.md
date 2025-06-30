# Two Pointer パターン

Two Pointerは配列や文字列を効率的に処理するための重要なアルゴリズムテクニックです。

## 概要

Two Pointerテクニックは、2つのポインタ（インデックス）を使って配列や文字列を走査する方法です。通常のネストしたループではO(n²)になる処理を、O(n)に削減できることが多いです。

## 主なパターン

### 1. 対向型（Opposite Direction）

- 両端から中央に向かって進む
- 例：回文判定、Two Sum（ソート済み）、Container With Most Water

```python
left, right = 0, len(array) - 1
while left < right:
    # 処理
    left += 1
    right -= 1
```

### 2. 同方向型（Same Direction）

- 両方のポインタが同じ方向に進む
- Fast/Slowポインタとも呼ばれる
- 例：重複除去、要素の移動、部分列判定

```python
slow = 0
for fast in range(len(array)):
    if condition:
        # slowの位置に要素を配置
        slow += 1
```

### 3. スライディングウィンドウ型

- 可変長または固定長のウィンドウを維持
- 例：部分配列の最大/最小、文字列の部分一致

## 使用する場面

- ソート済み配列での探索
- 配列の要素の並べ替えや削除（インプレース）
- 部分配列や部分文字列の問題
- 複数の要素の組み合わせを探す問題

## 利点

1. **時間効率**: O(n²)をO(n)に削減
2. **空間効率**: 通常O(1)の追加空間で実装可能
3. **シンプル**: コードが直感的で理解しやすい

## ファイル構成

- `basic_two_pointer.py`: 基本的なTwo Pointerパターンの実装
- `reverse_patterns.py`: 逆転操作に特化したパターン
- （今後追加予定）`sliding_window.py`: スライディングウィンドウパターン

## 練習問題

LeetCodeでTwo Pointerを使う代表的な問題：

-  3Sum
-  Container With Most Water
-  Valid Palindrome
-  Two Sum II - Input Array Is Sorted
-  Move Zeroes
-  Reverse String
-  Reverse Words in a String
