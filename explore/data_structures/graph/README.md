# グラフ (Graph)

頂点（ノード）と辺（エッジ）で構成される非線形データ構造です。

## 基本概念

### グラフの種類
1. **無向グラフ**: 辺に方向がない
2. **有向グラフ**: 辺に方向がある
3. **重み付きグラフ**: 辺に重み（コスト）がある
4. **非重み付きグラフ**: 全ての辺の重みが同じ

### グラフの性質
- **連結性**: 全ての頂点が繋がっているか
- **サイクル**: 閉路が存在するか
- **次数**: 頂点に接続する辺の数

## グラフの表現方法

### 1. 隣接行列 (Adjacency Matrix)
```python
# n×nの2次元配列
# graph[i][j] = 1 if edge exists from i to j
class GraphMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v, weight=1):
        self.graph[u][v] = weight
        # 無向グラフの場合
        # self.graph[v][u] = weight
    
    def has_edge(self, u, v):
        return self.graph[u][v] != 0
    
    def get_neighbors(self, vertex):
        neighbors = []
        for i in range(self.vertices):
            if self.graph[vertex][i] != 0:
                neighbors.append(i)
        return neighbors
```

**利点**: エッジの存在確認がO(1)
**欠点**: O(V²)のメモリ使用、疎なグラフで無駄

### 2. 隣接リスト (Adjacency List)
```python
from collections import defaultdict

class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, weight=1):
        self.graph[u].append((v, weight))
        # 無向グラフの場合
        # self.graph[v].append((u, weight))
    
    def get_neighbors(self, vertex):
        return self.graph[vertex]
    
    def has_edge(self, u, v):
        return any(neighbor[0] == v for neighbor in self.graph[u])
```

**利点**: メモリ効率的 O(V+E)、疎なグラフに適する
**欠点**: エッジの存在確認がO(次数)

### 3. エッジリスト (Edge List)
```python
class GraphEdgeList:
    def __init__(self):
        self.edges = []
    
    def add_edge(self, u, v, weight=1):
        self.edges.append((u, v, weight))
    
    def get_edges(self):
        return self.edges
```

**利点**: シンプル、Kruskal法に適する
**欠点**: 隣接頂点の取得が非効率

## グラフの基本操作

### 1. 頂点の追加・削除
```python
def add_vertex(self, vertex):
    if vertex not in self.graph:
        self.graph[vertex] = []

def remove_vertex(self, vertex):
    # 頂点とそれに関連する全ての辺を削除
    if vertex in self.graph:
        # その頂点への辺を削除
        for v in self.graph:
            self.graph[v] = [edge for edge in self.graph[v] 
                           if edge[0] != vertex]
        # 頂点自体を削除
        del self.graph[vertex]
```

### 2. 辺の追加・削除
```python
def remove_edge(self, u, v):
    if u in self.graph:
        self.graph[u] = [edge for edge in self.graph[u] 
                        if edge[0] != v]
```

### 3. 次数の計算
```python
def in_degree(self, vertex):
    """入次数（有向グラフ）"""
    count = 0
    for v in self.graph:
        for neighbor, _ in self.graph[v]:
            if neighbor == vertex:
                count += 1
    return count

def out_degree(self, vertex):
    """出次数（有向グラフ）"""
    return len(self.graph[vertex])

def degree(self, vertex):
    """次数（無向グラフ）"""
    return len(self.graph[vertex])
```

## 特殊なグラフ

### 1. 木 (Tree)
- 連結かつ非循環
- V個の頂点、V-1個の辺
- 任意の2頂点間にただ1つの経路

### 2. DAG (Directed Acyclic Graph)
- 有向かつ非循環
- トポロジカルソートが可能

### 3. 完全グラフ
- 全ての頂点対が辺で結ばれている
- V個の頂点でV(V-1)/2個の辺

### 4. 二部グラフ
- 頂点が2つのグループに分割可能
- 同じグループ内の頂点間に辺がない

## グラフの実装例

### 重み付き有向グラフ
```python
class WeightedDirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
    
    def get_weight(self, u, v):
        for neighbor, weight in self.graph[u]:
            if neighbor == v:
                return weight
        return float('inf')
    
    def get_vertices(self):
        return list(self.vertices)
    
    def get_edges(self):
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                edges.append((u, v, weight))
        return edges
```

## メモリ効率とパフォーマンス

### 隣接行列 vs 隣接リスト
| 操作 | 隣接行列 | 隣接リスト |
|------|----------|------------|
| 辺の存在確認 | O(1) | O(degree) |
| 隣接頂点の取得 | O(V) | O(degree) |
| 辺の追加 | O(1) | O(1) |
| 辺の削除 | O(1) | O(degree) |
| 空間計算量 | O(V²) | O(V+E) |

### 選択基準
- **密なグラフ**: 隣接行列
- **疎なグラフ**: 隣接リスト
- **エッジクエリが多い**: 隣接行列
- **メモリ制限がある**: 隣接リスト

## 典型的な問題
- Clone Graph
- Number of Islands
- Graph Valid Tree
- Number of Connected Components
- Course Schedule (Topological Sort)
- Alien Dictionary
- Graph Bipartiteness
- Redundant Connection
- Minimum Height Trees
- Evaluate Division