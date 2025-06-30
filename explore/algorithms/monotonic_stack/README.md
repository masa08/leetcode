# 単調スタック (Monotonic Stack)

スタック内の要素が単調増加または単調減少を保つスタックの応用パターンです。

## 基本概念

### 単調スタックの特徴

- **単調増加**: スタックの底から頂上へ値が増加
- **単調減少**: スタックの底から頂上へ値が減少
- **不変条件の維持**: push時に単調性を破る要素を除去

### 基本テンプレート

```python
def monotonic_stack_template(nums):
    stack = []  # インデックスを保存
    result = []
    
    for i, num in enumerate(nums):
        # 単調性を保つために要素を除去
        while stack and nums[stack[-1]] > num:  # 単調増加の場合
            result.append((stack.pop(), i))
        
        stack.append(i)
    
    return result
```

## 重要なパターン

### 1. Next Greater Element

```python
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            result[index] = num
        stack.append(i)
    
    return result
```

### 2. Daily Temperatures

- 各日について、より暖かい日までの日数
- Next Greater Elementの応用

### 3. Largest Rectangle in Histogram

```python
def largest_rectangle(heights):
    stack = []
    max_area = 0
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    # 残った要素を処理
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area
```

### 4. Maximal Rectangle

- 2D配列での最大矩形
- 各行でHistogram問題に変換

## 単調性の選択

### 単調増加スタック

- **用途**: Next Greater Element系
- **条件**: `stack[-1] >= current`で要素を除去

### 単調減少スタック

- **用途**: Next Smaller Element系
- **条件**: `stack[-1] <= current`で要素を除去

## 実装のコツ

### 1. インデックス vs 値

```python
# インデックスを保存（推奨）
stack.append(i)
while stack and nums[stack[-1]] > nums[i]:

# 値を保存（制限あり）
stack.append(nums[i])
while stack and stack[-1] > nums[i]:
```

### 2. 境界処理

- 配列の最後に番兵（sentinel）を追加
- スタックに残った要素の処理

### 3. 逆向き処理

- 右から左へスキャン
- Previous Greater/Smaller Element

## 計算量

- **時間計算量**: O(n) - 各要素は最大1回push/pop
- **空間計算量**: O(n) - スタックのサイズ

## 応用問題

### 1. 株価スパン

- 現在以下の価格が何日続いたか

### 2. 山脈配列

- 単調増加後に単調減少する配列

### 3. 水たまり問題

- Trapping Rain Water
- 2つの単調スタックまたは動的プログラミング

## 典型的な問題

-  Trapping Rain Water
-  Largest Rectangle in Histogram
-  Maximal Rectangle
-  Remove Duplicate Letters
-  Remove K Digits
-  Next Greater Element I
-  Next Greater Element II
-  Daily Temperatures
-  Online Stock Span
-  Sum of Subarray Minimums
-  Next Greater Node In Linked List
-  Count Submatrices With All Ones
