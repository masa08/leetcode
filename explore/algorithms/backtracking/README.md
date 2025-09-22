# バックトラッキング (Backtracking)

## 核心概念

バックトラッキングは「**試行錯誤の体系化**」です。行き止まりに到達したら一歩戻って別の道を試す、という探索方法です。

### 3つの本質的ステップ

1. **選択 (Choose)** - 可能な選択肢から一つ選ぶ
2. **探索 (Explore)** - その選択で再帰的に進む
3. **取消 (Unchoose)** - 選択を取り消して戻る

### メンタルモデル

```text
        []
      /    \
    [1]    [2]    → 選択
   /  \    /  \
[1,2][1,3][2,1]...→ 探索
  ↑              → 取消して別の道へ
```

## 基本テンプレート

```python
def backtrack(state):
    if is_solution(state):
        results.append(state[:])  # コピーを保存
        return

    for choice in get_choices(state):
        if not is_valid(state, choice):
            continue  # 枝刈り

        state.append(choice)      # 選択
        backtrack(state)           # 探索
        state.pop()                # 取消（重要！）
```

## 3つの主要パターン

### 1. 順列・組み合わせ

```python
def permutations(nums):
    result = []

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for num in nums:
            if num in path:
                continue
            path.append(num)
            backtrack(path)
            path.pop()

    backtrack([])
    return result
```

### 2. 部分集合

```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)  # i+1で重複回避
            path.pop()

    backtrack(0, [])
    return result
```

### 3. 制約付き探索（N-Queens）

```python
def solve_n_queens(n):
    def is_safe(positions, row, col):
        for i in range(row):
            # 同じ列 or 対角線上にあるか
            if positions[i] == col or \
               positions[i] - i == col - row or \
               positions[i] + i == col + row:
                return False
        return True

    def backtrack(row, positions):
        if row == n:
            solutions.append(positions[:])
            return

        for col in range(n):
            if is_safe(positions, row, col):
                positions[row] = col
                backtrack(row + 1, positions)
                # positions[row]は次のループで上書きされるため明示的な取消不要

    solutions = []
    backtrack(0, [-1] * n)
    return solutions
```

## よくある間違いと対策

### 1. 状態の復元忘れ

```python
# ❌ 間違い
path.append(choice)
backtrack(path)
# pop()忘れ

# ✅ 正解
path.append(choice)
backtrack(path)
path.pop()  # 必ず復元
```

### 2. 参照の保存

```python
# ❌ 間違い
result.append(path)  # 参照を保存

# ✅ 正解
result.append(path[:])  # コピーを保存
```

### 3. 無限ループ

```python
# ❌ 間違い
backtrack(index, path)  # indexが変わらない

# ✅ 正解
backtrack(i + 1, path)  # 進行を保証
```

## 最適化の要点

### 枝刈り（Pruning）

```python
# 早期に無効な選択肢を除外
if not is_valid(choice):
    continue  # この枝は探索しない
```

### 重複回避

```python
# ソートして同じ要素をスキップ
nums.sort()
if i > start and nums[i] == nums[i-1]:
    continue
```

## 使い分け

**バックトラッキングが適する場合：**

- 全ての解を列挙する必要がある
- 制約条件で早期に枝刈りできる
- 解空間が比較的小さい

**他の手法を検討すべき場合：**

- 最適解が1つだけ必要 → BFS, DP
- 部分問題の重複が多い → DP
- 解空間が巨大で枝刈りが効かない → 貪欲法, ヒューリスティック

## 計算量

- **時間**: O(分岐数^深さ) - 通常は指数時間
- **空間**: O(深さ) - 再帰スタック

## 代表的な問題

- [46. Permutations](https://leetcode.com/problems/permutations/)
- [78. Subsets](https://leetcode.com/problems/subsets/)
- [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
- [51. N-Queens](https://leetcode.com/problems/n-queens/)
- [79. Word Search](https://leetcode.com/problems/word-search/)
