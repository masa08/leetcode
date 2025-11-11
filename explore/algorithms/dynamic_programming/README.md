# 動的計画法 (Dynamic Programming)

動的計画法（DP）は、**ある状態における求めたい値を一度計算して記録し、それを再利用することで効率的に答えを求める手法**です。状態間の遷移に着目し、遷移式を立式できる場合に非常に効果的です。

## 核心概念

### 状態 (State) と遷移 (Transition)

- **状態**: ある状況や条件のこと。パラメータで一意に識別できる位置や状況（例: フィボナッチ数のN番目）
- **遷移**: 状態間の関係を表す式。ある状態の値を他の状態から求める方法

### DPが適用できる条件

1. **最適部分構造**: 問題の最適解が部分問題の最適解を含む
2. **重複する部分問題**: 同じ部分問題が複数回現れる

## 具体例: フィボナッチ数

N番目のフィボナッチ数を求める問題で理解しましょう。

### 遷移式の定義

```text
dp(N) = dp(N-1) + dp(N-2)
dp(0) = 1, dp(1) = 1
```

### 単純な再帰実装

```python
def dp(N: int) -> int:
    if N == 0 or N == 1:
        return 1
    return dp(N - 1) + dp(N - 2)
```

**問題点**:

- Time: O(2^N) - 同じ計算を何度も繰り返す
- Space: O(N) - 再帰スタックの深さ

例えば N=5 のとき、dp(2) を3回計算する無駄が発生します。

## 2つの実装アプローチ

### 1. メモ化 (Memoization) - Top-Down

再帰的に解き、計算結果をキャッシュして再利用。

```python
def fib(N: int, memo: dict = {}) -> int:
    # メモにあればそれを返す
    if N in memo:
        return memo[N]

    # 基本ケース
    if N <= 1:
        return 1

    # 計算してメモに保存
    memo[N] = fib(N-1, memo) + fib(N-2, memo)
    return memo[N]
```

**特徴**:

- 再帰を使用（元の問題から小さい問題へ）
- 必要な部分問題のみ解く
- 実装が直感的で遷移式をそのまま書ける

### 2. タブレーション (Tabulation) - Bottom-Up

小さい問題から順に解き、テーブルに結果を保存。

```python
def fib(N: int) -> int:
    if N <= 1:
        return 1

    # テーブル初期化
    dp = [0] * (N + 1)
    dp[0], dp[1] = 1, 1

    # 小さい問題から順に解く
    for i in range(2, N + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[N]
```

**特徴**:

- ループを使用（小さい問題から大きい問題へ）
- 全ての部分問題を解く
- 再帰のオーバーヘッドがない
- 通常はメモ化より高速

**改善後の計算量**: Time O(N), Space O(N)

## 主要パターン

### 1. 線形DP (1D DP)

1次元配列で状態を管理。前の要素から現在を計算。

**遷移の特徴**: `dp[i]` が `dp[i-1]`, `dp[i-2]` などから計算される

**典型問題**:

- Fibonacci Number
- Climbing Stairs (何通りの登り方があるか)
- House Robber (隣接する家は盗めない制約下での最大値)

**テンプレート**:

```python
dp = [0] * n
dp[0] = base_case
for i in range(1, n):
    dp[i] = max(dp[i-1] + nums[i], dp[i-2] + nums[i])
```

### 2. 2次元DP (2D DP)

2次元テーブルで状態を管理。2つのシーケンスやグリッドに関する問題。

**遷移の特徴**: `dp[i][j]` が `dp[i-1][j]`, `dp[i][j-1]`, `dp[i-1][j-1]` などから計算される

**典型問題**:

- Longest Common Subsequence (LCS) - 2つの文字列の最長共通部分列
- Edit Distance - 文字列の編集距離
- Unique Paths - グリッド上の経路数

**テンプレート (LCS)**:

```python
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

### 3. ナップサック問題 (Knapsack DP)

容量制限下での最適化問題。選択の組み合わせを求める。

**状態の定義**: `dp[i][w]` = 最初のi個のアイテムを使い、重さ制限wでの最大価値

**種類**:

- **0/1ナップサック**: 各アイテムを0回または1回使用
- **無制限ナップサック**: 各アイテムを何度でも使用可能

**典型問題**:

- Coin Change (最小コイン数)
- Partition Equal Subset Sum (配列を等分できるか)
- Target Sum

**テンプレート (0/1 Knapsack)**:

```python
dp = [[0] * (W+1) for _ in range(n+1)]
for i in range(1, n+1):
    for w in range(W+1):
        if weight[i-1] <= w:
            dp[i][w] = max(dp[i-1][w],
                          dp[i-1][w-weight[i-1]] + value[i-1])
        else:
            dp[i][w] = dp[i-1][w]
```

### 4. 最長増加部分列 (LIS - Longest Increasing Subsequence)

増加する部分列の最長を求める。

**状態の定義**: `dp[i]` = i番目の要素で終わるLISの長さ

**解法**:

- DP解法: O(n²)
- 二分探索+DP: O(n log n)

**典型問題**:

- Longest Increasing Subsequence
- Russian Doll Envelopes

**テンプレート (O(n²))**:

```python
dp = [1] * n
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
return max(dp)
```

### 5. 区間DP (Interval DP)

区間を考慮する問題。区間を分割して最適解を求める。

**状態の定義**: `dp[i][j]` = 区間 [i, j] における答え

**典型問題**:

- Matrix Chain Multiplication (行列の連鎖積)
- Palindrome Partitioning (回文分割)
- Burst Balloons

**テンプレート**:

```python
dp = [[0] * n for _ in range(n)]
for length in range(2, n+1):  # 区間の長さ
    for i in range(n - length + 1):
        j = i + length - 1
        for k in range(i, j):  # 分割点
            dp[i][j] = min(dp[i][j],
                          dp[i][k] + dp[k+1][j] + cost)
```

## 問題解決の流れ

1. **状態を定義する**: 何をパラメータとして問題を表すか
2. **遷移式を立てる**: 状態間の関係を数式で表す
3. **基本ケースを決める**: 初期値・境界条件
4. **実装方法を選ぶ**: メモ化 or タブレーション
5. **計算量を確認する**: Time/Space complexityが要件を満たすか

## 実装テンプレート

```python
class Solution:
    def dpProblem(self, params) -> int:
        # 1. エッジケース処理
        if not params:
            return 0

        # 2. DP配列の初期化
        n = len(params)
        dp = [0] * n  # または [[0] * m for _ in range(n)]

        # 3. 基本ケースの設定
        dp[0] = base_case

        # 4. 遷移式に基づいて計算
        for i in range(1, n):
            dp[i] = transition_function(dp, params, i)

        # 5. 結果を返す
        return dp[n-1]  # または dp全体から最大値など

def main():
    solution = Solution()

    # テストケース
    assert solution.dpProblem([1,2,3]) == expected
    print("All tests passed!")

if __name__ == "__main__":
    main()
```

## 計算量の改善

| 手法 | Time | Space | 特徴 |
|------|------|-------|------|
| 単純再帰 | O(2^N) | O(N) | 同じ計算を重複して実行 |
| メモ化 | O(N) | O(N) | 再帰+キャッシュ |
| タブレーション | O(N) | O(N) | ループで効率的 |

フィボナッチの例: N=40 で単純再帰は数秒かかるが、DP なら一瞬で終わる。

## 空間計算量の最適化

多くの場合、直前の数個の状態のみ必要なため、配列全体を保持する必要がない。

**例 (フィボナッチ)**:

```python
def fib(N: int) -> int:
    if N <= 1:
        return 1
    prev2, prev1 = 1, 1
    for i in range(2, N + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1
```

Space: O(N) → O(1) に改善

## 典型問題リスト

### 初級

- Fibonacci Number
- Climbing Stairs
- Min Cost Climbing Stairs

### 中級

- House Robber
- Coin Change
- Longest Increasing Subsequence
- Unique Paths
- Longest Common Subsequence

### 上級

- Edit Distance
- Longest Palindromic Substring
- Regular Expression Matching
- Burst Balloons
- Russian Doll Envelopes

## ファイル構成

- `knapsack.py`: ナップサック問題の実装例

## 参考

- [LeetCode DP Problems](https://leetcode.com/tag/dynamic-programming/)
- UMPIRE法を使った体系的なアプローチを推奨
