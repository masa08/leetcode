# 配列と文字列のアルゴリズム (Array & String Algorithms)

配列と文字列データ構造を使った問題解決パターンとテクニックです。

> **注意**: データ構造そのものについては `data_structures/array/` と `data_structures/string/` を参照してください。

## 基本操作

### 配列の操作

- インデックスアクセス: O(1)
- 挿入・削除: O(n)
- 探索: O(n)

### 文字列の操作

- Python文字列はimmutable
- 変更にはリスト変換が必要
- 文字列結合は効率に注意

## 重要なパターン

### 1. Two Pointers

- 対向ポインタ（両端から中央へ）
- 同方向ポインタ（Fast & Slow）

### 2. スライディングウィンドウ

- 固定長ウィンドウ
- 可変長ウィンドウ

### 3. 前缀和 (Prefix Sum)

- 範囲の合計を効率的に計算
- 2D配列での累積和

### 4. 文字列マッチング

- KMP法、Boyer-Moore法
- ローリングハッシュ

## 典型的な問題

-  Two Sum
-  Container With Most Water
-  3Sum
-  Remove Duplicates from Sorted Array
-  Remove Element
-  Valid Palindrome
-  Reverse Words in a String
-  Product of Array Except Self
-  Move Zeroes
-  Reverse String
-  Reverse Vowels of a String
-  Is Subsequence
-  String Compression
