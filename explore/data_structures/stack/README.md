# スタック (Stack)

LIFO（Last In First Out）の原則に従うデータ構造とその応用パターンです。

## 基本概念

### スタックの操作

- **Push**: 要素を追加 - O(1)
- **Pop**: 最上位要素を削除・取得 - O(1)
- **Peek/Top**: 最上位要素を参照 - O(1)
- **IsEmpty**: 空かどうか確認 - O(1)

### Pythonでの実装

```python
stack = []
stack.append(item)    # push
item = stack.pop()    # pop
top = stack[-1]       # peek
```

## 重要なパターン

### 1. 括弧の対応関係

- Valid Parentheses問題
- 開き括弧をpush、閉じ括弧でpopして検証

### 2. 単調スタック (Monotonic Stack)

- スタック内要素が単調増加/減少
- Next Greater Element問題
- Daily Temperatures問題

### 3. 式の評価

- 中置記法→後置記法変換
- 逆ポーランド記法の計算

### 4. 深さ優先探索(DFS)

- 再帰の代わりにスタックを使用
- 明示的なスタック管理

### 5. Undo機能

- 操作履歴の管理
- バックトラッキング

## 応用データ構造

- **関数呼び出しスタック**: 再帰処理
- **ブラウザの戻るボタン**: ページ履歴
- **エディタのUndo機能**: 操作履歴

## 典型的な問題

-  Valid Parentheses
-  Simplify Path
-  Evaluate Reverse Polish Notation
-  Min Stack
-  Basic Calculator
-  Decode String
-  Next Greater Element I
-  Daily Temperatures
-  Backspace String Compare
-  Remove All Adjacent Duplicates In String
-  Removing Stars From a String
