# バックトラッキング (Backtracking)

全ての可能性を体系的に探索し、条件に合わない場合は戻って別の選択肢を試すアルゴリズムです。

## 基本概念

### バックトラッキングの流れ

1. 選択肢を一つ選ぶ
2. その選択が有効かチェック
3. 有効なら次のステップへ進む
4. 無効または行き詰まったら選択を取り消して戻る
5. 他の選択肢を試す

### 基本テンプレート

```python
def backtrack(path, choices):
    # ベースケース（解を見つけた場合）
    if is_solution(path):
        result.append(path[:])  # コピーを保存
        return
    
    # 選択肢を試す
    for choice in choices:
        if is_valid(choice, path):
            # 選択
            path.append(choice)
            
            # 再帰
            backtrack(path, next_choices)
            
            # 選択を取り消し（バックトラック）
            path.pop()
```

## 重要なパターン

### 1. 順列・組み合わせ

- Permutations: 順序あり、重複なし
- Combinations: 順序なし、重複なし
- Combination Sum: 重複使用可能

### 2. 部分集合 (Subset)

- 全ての部分集合を生成
- 条件を満たす部分集合のみ

### 3. グリッド上の経路探索

- N-Queens問題
- Sudoku Solver
- Word Search

### 4. 分割問題

- Palindrome Partitioning
- Restore IP Addresses

## 最適化テクニック

### 1. 枝刈り (Pruning)

- 早期に無効な選択肢を除外
- 実行時間の大幅短縮

### 2. 重複回避

- ソートして同じ要素をスキップ
- visited配列で訪問済みをマーク

### 3. メモ化

- 部分問題の結果をキャッシュ
- 動的プログラミングとの組み合わせ

## 計算量

- 時間計算量: 通常は指数時間 O(k^n)
- 空間計算量: 再帰の深さに比例 O(n)

## 典型的な問題

-  Letter Combinations of a Phone Number
-  Generate Parentheses
-  Combination Sum
-  Combination Sum II
-  Permutations
-  Permutations II
-  N-Queens
-  Combinations
-  Subsets
-  Subsets II
-  Palindrome Partitioning
-  Combination Sum III
