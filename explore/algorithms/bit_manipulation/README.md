# ビット操作 (Bit Manipulation)

ビット演算を使った効率的なアルゴリズムとテクニックです。

## 基本演算

### ビット演算子

```python
# AND: 両方が1の時1
a & b

# OR: どちらかが1の時1  
a | b

# XOR: 異なる時1、同じ時0
a ^ b

# NOT: ビット反転
~a

# 左シフト: 2倍
a << 1

# 右シフト: 半分
a >> 1
```

### 基本的なトリック

```python
# 最下位ビットの取得
lowest_bit = n & (-n)

# 最下位ビットを削除
n & (n - 1)

# n番目ビットが1かチェック
(num >> n) & 1

# n番目ビットをセット
num | (1 << n)

# n番目ビットをクリア
num & ~(1 << n)

# n番目ビットを反転
num ^ (1 << n)
```

## 重要なパターン

### 1. ビットカウント

```python
def count_bits(n):
    count = 0
    while n:
        count += 1
        n &= n - 1  # 最下位の1ビットを削除
    return count

# Brian Kernighan's Algorithm
# bin(n).count('1') # Pythonの組み込み関数
```

### 2. 2の累乗判定

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

### 3. 唯一の数字を見つける

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # XORで重複を消去
    return result
```

### 4. 2つの唯一の数字

```python
def single_numbers(nums):
    xor = 0
    for num in nums:
        xor ^= num
    
    # 最下位の異なるビットを見つける
    diff = xor & (-xor)
    
    a = b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num
    
    return [a, b]
```

### 5. 部分集合の生成

```python
def generate_subsets(nums):
    n = len(nums)
    result = []
    
    for mask in range(1 << n):  # 2^n通り
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        result.append(subset)
    
    return result
```

## 高度なテクニック

### 1. ビットマスクDP

- 状態をビットで表現
- TSP (Traveling Salesman Problem)
- Assignment Problem

### 2. フェンウィック木 (Binary Indexed Tree)

- 範囲和クエリをO(log n)で処理
- ビット操作で親子関係を表現

### 3. ハミング距離

```python
def hamming_distance(x, y):
    return bin(x ^ y).count('1')
```

### 4. グレイコード

- 隣接する数字が1ビットだけ異なる
- `i ^ (i >> 1)` でi番目のグレイコード

## 実用的な応用

### 1. 権限管理

```python
READ = 1    # 001
WRITE = 2   # 010
EXECUTE = 4 # 100

# 権限の設定
permission = READ | WRITE  # 011

# 権限のチェック
has_read = permission & READ  # True if has read permission
```

### 2. 状態圧縮

- 小さな状態をビットで表現
- メモリ効率の向上

### 3. 高速演算

```python
# 偶数判定
is_even = (n & 1) == 0

# 符号反転
opposite = ~n + 1

# 絶対値（正の数のみ）
abs_val = (n ^ (n >> 31)) - (n >> 31)
```

## 注意点

1. **符号**: 負数の右シフトは実装依存
2. **オーバーフロー**: 大きな数でのシフト演算
3. **可読性**: ビット演算は理解が困難な場合がある

## 典型的な問題

-  Single Number
-  Single Number II
-  Reverse Bits
-  Number of 1 Bits
-  Power of Two
-  Single Number III
-  Missing Number
-  Maximum Product of Word Lengths
-  Counting Bits
-  Sum of Two Integers
-  Find the Difference
-  UTF-8 Validation
-  Maximum XOR of Two Numbers in an Array
-  Hamming Distance
