# Explore - アルゴリズムとデータ構造

このディレクトリには、LeetCode問題解決に必要なアルゴリズムとデータ構造の実装とパターンが整理されています。

## 分類の基準

### **データ構造 (data_structures/)**
**"どう格納するか"（What to store）**
- データの組織化と格納方法
- 基本操作（挿入、削除、探索、更新）
- メモリレイアウトと効率性

### **アルゴリズム (algorithms/)**
**"どう処理するか"（How to process）**
- データ構造を使った問題解決手法
- 特定の計算手順やテクニック
- 最適化戦略とパターン

## データ構造 (data_structures/)

### 線形データ構造
- **array/** - 配列の基本操作と応用
- **string/** - 文字列処理とアルゴリズム
- **linked_list/** - 連結リストの実装と操作
- **stack/** - スタック（LIFO）の応用
- **queue/** - キュー（FIFO）の応用

### 非線形データ構造
- **binary_tree/** - 二分木の走査と操作
- **binary_search_tree/** - BST の特性と応用
- **heap/** - ヒープ（優先度付きキュー）
- **graph/** - グラフの表現と基本操作

### 高度なデータ構造
- **hash_map/** - ハッシュテーブルの活用
- **trie/** - トライ木（接頭辞木）

## アルゴリズム (algorithms/)

### 基本テクニック
- **two_pointer/** - Two Pointerテクニック
- **binary_search/** - 二分探索とその変形
- **sorting/** - ソートアルゴリズムの比較

### 問題解決パターン
- **backtracking/** - バックトラッキング
- **greedy/** - グリーディアルゴリズム
- **dynamic_programming/** - 動的プログラミング

### 特殊なテクニック
- **bit_manipulation/** - ビット操作
- **monotonic_stack/** - 単調スタック
- **intervals/** - 区間問題
- **graph_algorithms/** - グラフアルゴリズム

## 学習の進め方

1. **データ構造から開始**: まず基本的なデータ構造の理解
2. **アルゴリズムの習得**: データ構造を使った問題解決手法
3. **パターンの認識**: 類似問題での応用
4. **実装と練習**: 各ディレクトリの典型問題で練習

## ディレクトリ構成

各ディレクトリには以下が含まれています：
- **README.md**: 概念説明、実装例、典型問題
- **実装ファイル**: 基本的なパターンの実装
- **サンプルコード**: 使用例とテスト

## 相互関係

多くのアルゴリズムは複数のデータ構造を組み合わせて使用します：
- **グラフアルゴリズム** ← グラフ + キュー/スタック
- **動的プログラミング** ← 配列 + ハッシュマップ
- **二分探索** ← 配列 + ソート
- **バックトラッキング** ← スタック + 再帰