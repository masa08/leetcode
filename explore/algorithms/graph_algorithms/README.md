# グラフアルゴリズム (Graph Algorithms)

グラフデータ構造に対する探索、最短経路、連結性などを扱うアルゴリズム群です。

## 基本的なグラフ探索

### 1. 深さ優先探索 (DFS)

- スタックまたは再帰を使用
- 経路の存在確認、サイクル検出に有効

### 2. 幅優先探索 (BFS)

- キューを使用
- 最短経路（重みなしグラフ）の発見に有効

## 高度なアルゴリズム

### 1. 最短経路アルゴリズム

- **Dijkstra法**: 非負の重みを持つグラフでの単一始点最短経路
- **Bellman-Ford法**: 負の重みも扱える
- **Floyd-Warshall法**: 全点対最短経路

### 2. Union-Find（素集合データ構造）

- **Quick Find**: 検索がO(1)、結合がO(n)
- **Quick Union**: より効率的な結合操作
- **Path Compression付きUnion-Find**: 最適化版

### 3. 最小全域木

- **Kruskal法**: 辺を重みでソート
- **Prim法**: 頂点を基準に成長

## ファイル構成

- `dijkstras.py`: Dijkstra法の実装
- `quick_find_example.py`: Quick Findの実装
- `quick_union.py`: Quick Unionの実装

## 典型的な問題

- Number of Islands
- Course Schedule
- Clone Graph
- Number of Provinces
- Network Delay Time
- Min Cost to Connect All Points
