# CLAUDE.md

LeetCodeソリューションリポジトリのClaude Code向けガイドライン。

## リポジトリ構造

```text
leetcode/
├── solutions/        # 問題番号で管理（例: 1_two_sum.py）
├── model/           # 共通データ構造（ListNode, TreeNode）
├── utils/           # ヘルパー関数
└── explore/         # パターンの抽象化
    ├── algorithms/  # アルゴリズム手法
    └── data_structures/  # データ構造実装
```

## 学習リソース

1. **[LeetCode 75](https://leetcode.com/studyplan/leetcode-75/)** - 基礎固め
2. **[Top Interview 150](https://leetcode.com/studyplan/top-interview-150/)** - 面接頻出問題
3. **Cracking the Coding Interview** - 体系的学習

## コーディング原則

### 最重要5原則

#### 1. **UMPIRE法** - 体系的問題解決

```text
U - Understand: 問題理解、エッジケース列挙
M - Match: 既知パターンとマッチング
P - Plan: アプローチ説明、計算量分析
I - Implement: クリーンな実装
R - Review: コードウォークスルー
E - Evaluate: 時間/空間計算量の確認
```

💡 思考プロセスの明確さ、質問力、エッジケース考慮

#### 2. **エッジファースト** - 防御的プログラミング

```python
def solve(nums: List[int]) -> int:
    # エッジケースを最初に処理
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # メインロジック
    # ...
```

💡 堅牢性、プロダクションレディなコード

#### 3. **段階的最適化** - 正確性から効率性へ

```python
# Step 1: ブルートフォース O(n²)
def twoSum_v1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Step 2: 最適化 O(n)
def twoSum_v2(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
```

💡 最適化能力、トレードオフの理解

#### 4. **パターン認識** - 高頻度テクニック

- **Two Pointers**: ソート済み配列、ペア探索
- **Sliding Window**: 部分配列、部分文字列
- **Hash Map**: O(1)ルックアップ
- **DFS/BFS**: グラフ、ツリー探索
- **Dynamic Programming**: 最適化問題

💡 問題解決の効率性、パターン適用力

#### 5. **明確性優先** - 可読性とコミュニケーション

```python
# 悪い例
def fn(a, n):
    i, j = 0, n-1
    while i < j:
        # ...

# 良い例  
def findPair(arr: List[int], target: int) -> List[int]:
    left, right = 0, len(arr) - 1
    while left < right:
        # Two pointersで目標値のペアを探索
```

💡 チーム開発能力、保守性への配慮

### 実装ガイドライン

```python
class Solution:
    def methodName(self, params) -> ReturnType:
        # 1. エッジケース処理（エッジファースト）
        if not params:
            return default_value
        
        # 2. アプローチの選択（パターン認識）
        # 例：Two Pointers, Hash Map等
        
        # 3. メインロジック（明確な変数名）
        result = self.helper(params)
        
        # 4. 結果を返す
        return result
    
    def helper(self, data):
        """ヘルパー関数には明確な責務を"""
        pass

def main():
    # テストケース（基本、エッジ、大規模）
    solution = Solution()
    
    # 基本ケース
    assert solution.methodName([1,2,3]) == expected
    
    # エッジケース
    assert solution.methodName([]) == default
    assert solution.methodName([1]) == single_element_result
    
    print("All tests passed!")
    
if __name__ == "__main__":
    main()
```

## 面接での対話方針

- **直接答えない** - ヒントを与えて思考を促す
- **時間/空間計算量** - 常に議論する
- **エッジケース** - 見落としを指摘する
- **最適化** - より良い解法の可能性を探る

## 問題解決の流れ

1. **理解** - 入出力例を確認、エッジケースを列挙
2. **設計** - アプローチを説明、計算量を分析
3. **実装** - シンプルで明確なコードを書く
4. **改善** - 最適化の余地を検討

## 重要な判断基準

- **可読性 > 巧妙さ** - 面接では理解しやすさが重要
- **標準ライブラリ** - 基本的なものは使用OK（Counter等は説明付きで）
- **トレードオフ** - 時間vs空間、実装の複雑さvs効率性を明確に
