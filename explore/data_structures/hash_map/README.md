# ハッシュマップ・ハッシュセット (Hash Map & Hash Set)

ハッシュテーブルを使った効率的なデータの格納と検索パターンです。

## 基本概念

### ハッシュマップ (Dictionary)

- キー→値のマッピング
- 平均的にO(1)でアクセス・挿入・削除
- Pythonでは`dict`

### ハッシュセット (Set)

- 重複のない要素の集合
- 平均的にO(1)で存在確認・挿入・削除
- Pythonでは`set`

## 重要なパターン

### 1. 出現回数のカウント

```python
from collections import Counter
count = Counter(array)
```

### 2. インデックスマッピング

- Two Sum問題での値→インデックス保存
- 過去に見た要素の記録

### 3. グループ化

- 文字列のアナグラム判定
- 数値の桁順による分類

### 4. 累積和とハッシュ

- Subarray Sumの効率的な計算

## 計算量の注意点

- 最悪ケース: O(n)（ハッシュ衝突）
- 平均ケース: O(1)
- スペース: O(n)

## 典型的な問題

-  Two Sum
-  Group Anagrams
-  Longest Consecutive Sequence
-  Contains Duplicate
-  Valid Anagram
-  Word Pattern
-  Ransom Note
-  Subarray Sum Equals K
-  Unique Number of Occurrences
-  Determine if Two Strings Are Close
-  Find the Difference of Two Arrays
