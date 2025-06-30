# グリーディアルゴリズム (Greedy Algorithm)

各ステップで局所最適な選択をして、全体最適解を目指すアルゴリズムです。

## 基本概念

### グリーディの特徴

- **局所最適選択**: その時点で最良の選択
- **選択の不可逆性**: 一度選択したら変更しない
- **最適部分構造**: 部分問題の最適解が全体の最適解に寄与

### 適用条件

1. **グリーディ選択特性**: 局所最適選択が全体最適につながる
2. **最適部分構造**: 問題が部分問題に分解できる

## 重要なパターン

### 1. スケジューリング問題

```python
# Activity Selection (終了時間でソート)
def activity_selection(activities):
    activities.sort(key=lambda x: x[1])  # 終了時間でソート
    selected = [activities[0]]
    last_end = activities[0][1]
    
    for start, end in activities[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    
    return selected
```

### 2. 最小スパニングツリー

- Kruskal法: 辺を重みでソート
- Prim法: 最小重みの辺を追加

### 3. 区間問題

- Meeting Rooms: 重複しない最大区間数
- Merge Intervals: 重複する区間の統合

### 4. ハフマン符号化

- 最小頻度のノードから結合
- 最適な符号長を実現

### 5. フラクショナルナップサック

- アイテムを分割可能
- 価値/重量比でソート

## vs 動的プログラミング

### グリーディが適用可能

- 局所最適 = 全体最適が保証される
- 例: コイン問題（貪欲法で解ける硬貨システム）

### DPが必要

- 局所最適 ≠ 全体最適
- 例: 0/1ナップサック問題

## 証明の考え方

1. **Exchange Argument**: グリーディ解を最適解に変換可能
2. **Greedy Stays Ahead**: グリーディが常に最適解以上
3. **Cut and Paste**: 最適解をグリーディ解に変換

## 実装のコツ

1. **適切なソート**: 判断基準を明確に
2. **貪欲選択の正当性**: なぜその選択が最適か
3. **エッジケースの処理**: 空集合、単一要素など

## 典型的な問題

-  Jump Game II
-  Jump Game
-  Best Time to Buy and Sell Stock II
-  Gas Station
-  Candy
-  Course Schedule (Topological Sort)
-  Meeting Rooms II
-  Non-overlapping Intervals
-  Minimum Number of Arrows to Burst Balloons
-  Can Place Flowers
-  Task Scheduler
-  Valid Parenthesis String
-  Best Time to Buy and Sell Stock with Transaction Fee
-  Partition Labels
