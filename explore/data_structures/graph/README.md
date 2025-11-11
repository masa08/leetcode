# グラフ (Graph)

本セクションでは二分木で扱った内容を前提とします。まずはグラフとは何かについて改めて確認しましょう。

## グラフとは

グラフとは「対象とそれらの間でのつながりを表すデータ構造」です。頂点（ノード）と辺（エッジ）で構成される非線形データ構造で、様々な関係性をモデル化できます。

### 用語の定義

- **ノード (node / vertex / 頂点)**: グラフにおける「対象」。図では丸で表される
- **エッジ (edge / 辺)**: ノード同士の「つながり」や「関係」。図ではノード間を結ぶ線で表される

本ドキュメントでは基本的に**ノード**と**エッジ**で呼称します。

### 現実世界での応用例

グラフは抽象的な概念ですが、現実世界の様々な関係性を自然に表現できます:

| 具体例 | ノード | エッジ |
|--------|--------|--------|
| SNS | 人（ユーザー） | 友人関係・フォロー関係 |
| 道路網 | 交差点・都市 | 道路・距離 |
| Webページ | Webページ | ハイパーリンク |
| 履修システム | 科目 | 履修の前提条件 |
| コンピュータネットワーク | コンピュータ | 通信回線 |

## グラフの分類

グラフは**向き**と**重み**によって大まかに以下の4つに分類されます。この概念は二分木のセクションでは扱いませんでしたが、非常に重要なのでしっかり理解しましょう。

|  | 重みなし | 重みあり |
|---|---------|---------|
| **無向** | 重みなし無向グラフ | 重みあり無向グラフ |
| **有向** | 重みなし有向グラフ | 重みあり有向グラフ |

### 1. 重みなし無向グラフ (Unweighted Undirected Graph)

**無向グラフ**とは、エッジに方向性がないグラフです。つまり、ノードA-B間のエッジは双方向に移動可能です。

#### 無向グラフの具体例: SNSの友人関係

友人関係は相互的です。AliceがBobの友人ならば、BobもAliceの友人です。

```text
     Alice --- Bob
       |        |
     Paul     Chris
       |        |
     Lay ---- Ben --- Shelly
              |
            Steve
```

```python
# Alice: 0, Ben: 1, Bob: 2, Chris: 3, Lay: 4, Paul: 5, Shelly: 6, Steve: 7
graph = {
    0: [2, 4, 5],  # Alice と友人関係
    1: [3, 6, 7],  # Ben と友人関係
    2: [0, 4],     # Bob と友人関係
    3: [1],        # Chris と友人関係
    4: [0, 2],     # Lay と友人関係
    5: [0],        # Paul と友人関係
    6: [1],        # Shelly と友人関係
    7: [1],        # Steve と友人関係
}
```

#### 無向グラフの特徴

- エッジに方向がない（双方向に移動可能）
- エッジに重み（コスト）がない（全て等価）

### 2. 重みなし有向グラフ (Unweighted Directed Graph)

**有向グラフ**とは、エッジに方向性があるグラフです。A→Bのエッジがあっても、B→Aのエッジは別に存在する必要があります。

#### 有向グラフの具体例: 履修システムの前提科目

科目間の履修順序は一方向的です。数学Aを履修してから数学Bを履修できますが、逆はできません。

```text
    数学A
    /   \
   ↓     ↓
  数学B  数学C
   ↓       ↓
 物理基礎  |
    \    /
     ↓  ↓
    物理応用
```

```python
# 数学A: 0, 数学B: 1, 数学C: 2, 物理基礎: 3, 物理応用: 4
graph = {
    0: [1, 2],  # 数学A → 数学B, 数学C
    1: [3],     # 数学B → 物理基礎
    2: [4],     # 数学C → 物理応用
    3: [4],     # 物理基礎 → 物理応用
    4: [],      # 物理応用（終点）
}
```

#### 有向グラフの特徴

- エッジに方向がある（一方向のみ移動可能）
- エッジに重み（コスト）がない

#### 重要な用語

- **入次数 (in-degree)**: あるノードに入ってくるエッジの数
- **出次数 (out-degree)**: あるノードから出ていくエッジの数

例: 物理応用の入次数は2（数学Cと物理基礎から）、出次数は0

### 3. 重みあり無向グラフ (Weighted Undirected Graph)

**重み**とは、エッジに付与されるコストや距離などの値です。これによってノード間の関連の強さや距離を表現できます。

#### 重み付き無向グラフの具体例: 都市間の道路網

各都市間の距離は双方向で同じですが、距離（重み）が異なります。

```text
    A ---5--- B
    |         |
    3         4
    |         |
    D ---9--- C
    |
    2
    |
    E
```

```python
# A: 0, B: 1, C: 2, D: 3, E: 4
# (隣接ノード, 距離) のタプルで表現
graph = {
    0: [(1, 5), (3, 3)],           # A-B: 5, A-D: 3
    1: [(0, 5), (2, 4)],           # B-A: 5, B-C: 4
    2: [(1, 4)],                   # C-B: 4
    3: [(0, 3), (1, 9), (4, 2)],   # D-A: 3, D-B: 9, D-E: 2
    4: [(3, 2)],                   # E-D: 2
}
```

#### 重み付き無向グラフの特徴

- エッジに方向がない（双方向）
- エッジに重み（距離やコスト）がある
- 最短経路問題などで重要

### 4. 重みあり有向グラフ (Weighted Directed Graph)

有向グラフに重みが付いたものです。方向によって異なる重みを持つことができます。

#### 重み付き有向グラフの具体例: 一方通行を含む道路網

```text
    A --5→ B --4→ C
    ↑      ↓
    3      9
    ↑      ↓
    D ←----+
    |
    2
    ↓
    E

    F --5→ G
    ↑      |
    10←----+
```

地点Aから地点Bへは距離5で直接行けますが、地点Bから地点Aへは直接行けません（B→D→A で距離12が必要）。

地点F→Gは距離5ですが、G→Fは距離10です（一方通行ではなく、方向によって異なる道路）。

```python
# A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6
# (隣接ノード, 距離) のタプルで表現
graph = {
    0: [(1, 5)],        # A → B: 5
    1: [(2, 4), (3, 9)], # B → C: 4, B → D: 9
    2: [],              # C（終点）
    3: [(0, 3), (4, 2)], # D → A: 3, D → E: 2
    4: [],              # E（終点）
    5: [(6, 5)],        # F → G: 5
    6: [(5, 10)],       # G → F: 10
}
```

#### 重み付き有向グラフの特徴

- エッジに方向がある
- エッジに重みがある
- 最も一般的で表現力の高いグラフ形式
- ダイクストラ法などの最短経路アルゴリズムで使用

## グラフの表現方法

グラフをプログラムで扱う際、主に以下の2つのデータ構造を使用します。それぞれに利点と欠点があり、問題の性質に応じて使い分けます。

### 1. 隣接行列 (Adjacency Matrix)

**全てのノード同士の関係を2次元配列（行列）で表現**するデータ構造です。

#### 隣接行列の概念

n個のノードがある場合、n×nの2次元配列を作成し、`matrix[i][j]`にノードiからノードjへのエッジ情報を格納します。

- **重みなしグラフ**: エッジの有無を`True/False`または`1/0`で表現
- **重みありグラフ**: エッジの重みを数値で表現、エッジが無い場合は`float('inf')`や`None`

#### 隣接行列の具体例: 友人関係グラフ

グラフ分類セクションで紹介した友人関係グラフを、隣接行列で表現します。

| | Alice | Ben | Bob | Chris | Lay | Paul | Shelly | Steve |
|---|-------|-----|-----|-------|-----|------|--------|-------|
| **Alice** | - | False | True | False | True | True | False | False |
| **Ben** | False | - | False | True | False | False | True | True |
| **Bob** | True | False | - | False | True | False | False | False |
| **Chris** | False | True | False | - | False | False | False | False |
| **Lay** | True | False | True | False | - | False | False | False |
| **Paul** | True | False | False | False | False | - | False | False |
| **Shelly** | False | True | False | False | False | False | - | False |
| **Steve** | False | True | False | False | False | False | False | - |

```python
# Alice: 0, Ben: 1, Bob: 2, Chris: 3, Lay: 4, Paul: 5, Shelly: 6, Steve: 7
# 自分自身との関係はNoneで表現
graph = [
    [None, False, True, False, True, True, False, False],   # Alice
    [False, None, False, True, False, False, True, True],   # Ben
    [True, False, None, False, True, False, False, False],  # Bob
    [False, True, False, None, False, False, False, False], # Chris
    [True, False, True, False, None, False, False, False],  # Lay
    [True, False, False, False, False, None, False, False], # Paul
    [False, True, False, False, False, False, None, False], # Shelly
    [False, True, False, False, False, False, False, None], # Steve
]

# AliceとBobの友人関係を確認: O(1)
is_friend = graph[0][2]  # True
```

#### 隣接行列の応用例: 重み付き有向グラフ

グラフ分類セクションで紹介した一方通行を含む道路網を隣接行列で表現すると以下のようになります：

```python
# A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6
# エッジが無い場合はfloat('inf')、自分自身は0
graph = [
    [0, 5, float("inf"), float("inf"), float("inf"), float("inf"), float("inf")],  # A
    [float("inf"), 0, 4, 9, float("inf"), float("inf"), float("inf")],  # B
    [float("inf"), float("inf"), 0, float("inf"), float("inf"), float("inf"), float("inf")],  # C
    [3, float("inf"), float("inf"), 0, 2, float("inf"), float("inf")],  # D
    [float("inf"), float("inf"), float("inf"), float("inf"), 0, float("inf"), float("inf")],  # E
    [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 0, 5],  # F
    [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 10, 0],  # G
]

# A→Bの距離を確認: O(1)
distance = graph[0][1]  # 5

# B→Aの距離を確認: O(1)
distance = graph[1][0]  # inf (直接行けない)
```

#### 隣接行列の実装例

```python
class GraphMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        """エッジを追加"""
        self.graph[u][v] = weight
        # 無向グラフの場合
        # self.graph[v][u] = weight

    def has_edge(self, u, v):
        """エッジの存在確認 O(1)"""
        return self.graph[u][v] != 0

    def get_neighbors(self, vertex):
        """隣接ノードを取得 O(V)"""
        neighbors = []
        for i in range(self.vertices):
            if self.graph[vertex][i] != 0:
                neighbors.append(i)
        return neighbors
```

#### 隣接行列の特徴

**利点:**

- エッジの存在確認が**O(1)**で高速
- 実装がシンプルで直感的
- ノード間の関係を一目で把握できる

**欠点:**

- 空間計算量が**O(V²)**（Vはノード数）
- ノードが増えるとメモリ使用量が急増
- 疎なグラフ（エッジが少ない）では大部分が無駄

### 2. 隣接リスト (Adjacency List)

**各ノードに対して、そのノードと繋がっているノード（隣接ノード）のみをリストで保存**するデータ構造です。

#### 隣接リストの概念

各ノードiに対して、`list[i]`にはノードiから直接到達可能なノードのリストを格納します。

- **重みなしグラフ**: 隣接ノードの番号のみを格納
- **重みありグラフ**: `(隣接ノード, 重み)`のタプルを格納

#### 隣接リストの具体例: 友人関係グラフ

グラフ分類セクションで紹介した友人関係グラフを、隣接リストで表現します。

```python
# Alice: 0, Ben: 1, Bob: 2, Chris: 3, Lay: 4, Paul: 5, Shelly: 6, Steve: 7
graph = {
    0: [2, 4, 5],  # Aliceの友人: Bob, Lay, Paul
    1: [3, 6, 7],  # Benの友人: Chris, Shelly, Steve
    2: [0, 4],     # Bobの友人: Alice, Lay
    3: [1],        # Chrisの友人: Ben
    4: [0, 2],     # Layの友人: Alice, Bob
    5: [0],        # Paulの友人: Alice
    6: [1],        # Shellyの友人: Ben
    7: [1],        # Steveの友人: Ben
}

# Aliceの友人一覧を取得: O(1)
alice_friends = graph[0]  # [2, 4, 5]

# AliceとBobの友人関係を確認: O(V)最悪ケース
is_friend = 2 in graph[0]  # True
```

#### 隣接リストの応用例: 重み付き有向グラフ

グラフ分類セクションで紹介した一方通行を含む道路網を隣接リストで表現すると以下のようになります：

```python
# A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6
# (隣接ノード, 距離) のタプルで表現
graph = {
    0: [(1, 5)],        # A → B: 5
    1: [(2, 4), (3, 9)], # B → C: 4, B → D: 9
    2: [],              # C（終点）
    3: [(0, 3), (4, 2)], # D → A: 3, D → E: 2
    4: [],              # E（終点）
    5: [(6, 5)],        # F → G: 5
    6: [(5, 10)],       # G → F: 10
}

# Aの隣接ノードを取得: O(1)
neighbors = graph[0]  # [(1, 5)]

# A→Bの距離を確認: O(V)最悪ケース
for neighbor, weight in graph[0]:
    if neighbor == 1:
        distance = weight  # 5
```

#### 隣接リストの実装例

```python
from collections import defaultdict

class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight=1):
        """エッジを追加 O(1)"""
        self.graph[u].append((v, weight))
        # 無向グラフの場合
        # self.graph[v].append((u, weight))

    def get_neighbors(self, vertex):
        """隣接ノードを取得 O(1)"""
        return self.graph[vertex]

    def has_edge(self, u, v):
        """エッジの存在確認 O(V)最悪ケース、平均O(degree)"""
        return any(neighbor[0] == v for neighbor in self.graph[u])
```

#### 隣接リストの特徴

**利点:**

- 空間計算量が**O(V+E)**でメモリ効率的（V: ノード数、E: エッジ数）
- 疎なグラフ（エッジが少ない）に適している
- 隣接ノードの列挙が高速

**欠点:**

- エッジの存在確認が**O(V)最悪ケース**（平均O(degree)）
- 隣接行列より実装が少し複雑

### 3. エッジリスト (Edge List)

全てのエッジを`(始点, 終点, 重み)`のタプルのリストとして保存する方法です。

```python
class GraphEdgeList:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight=1):
        self.edges.append((u, v, weight))

    def get_edges(self):
        return self.edges

# 例
edges = [
    (0, 1, 5),  # A → B: 5
    (1, 2, 4),  # B → C: 4
    (1, 3, 9),  # B → D: 9
    (3, 0, 3),  # D → A: 3
    (3, 4, 2),  # D → E: 2
]
```

**利点**: シンプル、Kruskal法（最小全域木）に適する
**欠点**: 隣接頂点の取得が非効率

### 表現方法の選択基準

| 操作 | 隣接行列 | 隣接リスト | エッジリスト |
|------|----------|------------|-------------|
| エッジの存在確認 | **O(1)** | O(V) 最悪、平均O(degree) | O(E) |
| 隣接ノードの取得 | O(V) | **O(1)** | O(E) |
| エッジの追加 | **O(1)** | **O(1)** | **O(1)** |
| エッジの削除 | **O(1)** | O(degree) | O(E) |
| 全ノード訪問 | O(V²) | **O(V+E)** | O(VE) |
| 空間計算量 | O(V²) | **O(V+E)** | **O(E)** |

#### 選択の指針

| 状況 | 推奨 |
|------|------|
| **疎なグラフ**（エッジが少ない） | 隣接リスト |
| **密なグラフ**（エッジが多い） | 隣接行列 |
| **エッジクエリが頻繁** | 隣接行列 |
| **メモリ制限が厳しい** | 隣接リスト |
| **最小全域木アルゴリズム** | エッジリスト |

**LeetCodeでは基本的に隣接リストを使用します。** 多くの問題ではグラフのエッジ数が少なく（疎行列）、隣接行列では大部分が無駄になります。また、空間計算量O(V²)はノード数が大きいと扱うのが困難です。

## グラフの性質

### 1. 連結性 (Connectivity)

**連結**とは、任意のノード同士を繋ぐ経路が存在することです。

```text
連結グラフ:          非連結グラフ:
  A --- B              A --- B     E --- F
  |     |                            |
  C --- D              C --- D       G

全てのノードが        3つの独立した
1つのグループ        グループに分離
```

- **連結グラフ**: 全てのノードが互いに到達可能
- **連結成分 (Connected Component)**: 連結な部分グラフの最大単位

### 2. 閉路・サイクル (Cycle)

**閉路**とは、あるノードから出発してエッジを通って元のノードに戻って来れる経路です。

```text
閉路あり:            閉路なし（木）:
  A --- B              A --- B
  |     |              |     |
  C --- D              C     D
                       |
                       E
```

### 3. 次数 (Degree)

ノードに接続するエッジの数を**次数 (degree)**と呼びます。グラフの構造を分析する上で重要な概念です。

#### 無向グラフ

- **次数 (degree)**: ノードに接続するエッジの総数

**特殊なケース**:

- 次数0: **孤立ノード** (isolated vertex) - どのノードとも繋がっていない
- 次数1: **葉ノード** (leaf vertex) - 1つのノードとのみ繋がっている

#### 有向グラフ

- **入次数 (in-degree)**: ノードに入ってくるエッジの数
- **出次数 (out-degree)**: ノードから出ていくエッジの数
- **次数 (degree)**: 入次数 + 出次数

**握手補題 (Handshaking Lemma)**: 無向グラフにおいて、全ノードの次数の合計は常にエッジ数の2倍に等しい（各エッジが2つのノードに寄与するため）

```python
def in_degree(graph, vertex):
    """入次数（有向グラフ）"""
    count = 0
    for v in graph:
        for neighbor, _ in graph[v]:
            if neighbor == vertex:
                count += 1
    return count

def out_degree(graph, vertex):
    """出次数（有向グラフ）"""
    return len(graph[vertex])

def degree(graph, vertex):
    """次数（無向グラフ）"""
    return len(graph[vertex])
```

## Tree（木構造）とグラフの関係

### 木の定義

二分木のセクションで学んだ木構造は、実はグラフの特殊なケースです。

#### 木の直感的な定義

- ルートノード（根）から階層的に枝分かれする構造
- 親ノードと子ノードの関係（親は複数の子を持てるが、子の親は1つ）
- 末端のノードをリーフ（葉）と呼ぶ

#### 木の厳密な定義

木とは、無向グラフにおいて以下の条件を満たすものです。実は以下の条件は**すべて等価**です（どれか1つを満たせば他も自動的に満たされる）:

1. **連結かつ閉路なし**: 全てのノードが繋がっており、どのノードからも元のノードに戻れない
2. **連結かつV個のノードにV-1個のエッジ**: 連結グラフでエッジ数がノード数より1少ない
3. **閉路なしかつV個のノードにV-1個のエッジ**: 閉路がなく、エッジ数がノード数より1少ない
4. **任意の2ノード間にただ1つの経路**: どの2つのノードも、ちょうど1通りの経路で結ばれる

```text
木（Tree）:              木ではない:
    A                    A --- B        閉路がある
   / \                   |     |
  B   C                  C --- D
 / \  \
D  E   F                 A   B   C     連結でない

                         D --- E
```

### 木の特徴

#### 特徴1: エッジ数は必ず V-1 （Vはノード数）

木を根から作っていくことを考えると理解できます:

```text
Step 1: 根のみ
   A
   ノード数: 1, エッジ数: 0

Step 2: 子を1つ追加
   A
   |
   B
   ノード数: 2, エッジ数: 1

Step 3: さらに子を追加
   A
  / \
 B   C
 ノード数: 3, エッジ数: 2
```

根から木を作ると、**新しいノードを追加する度に必ずエッジも1つ追加**されます。よって根を除いたノード数とエッジ数は常に等しく、根を含めると**エッジ数 = ノード数 - 1**となります。

#### 特徴2: 任意のノードは根となり得る

木では、どのノードを根と見なしても木として成立します。

```text
根をAとした場合:       根をBとした場合:
    A                     B
   / \                   /|\
  B   C                 A D E
 /|\                    |
D E F                   C
                        |
                        F
```

これらは全く同じ構造ですが、根の選び方によって見え方が変わります。

#### 木の判定条件

グラフが木かどうかを判定するには:

```python
def is_tree(n, edges):
    """
    n: ノード数
    edges: エッジのリスト [(u, v), ...]
    """
    # 条件1: エッジ数がn-1であること
    if len(edges) != n - 1:
        return False

    # 条件2: 連結であること（DFS/BFSで全ノードに到達可能）
    # 条件3: 閉路が無いこと（連結 + エッジ数n-1で保証される）

    # グラフを構築
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # DFSで連結性を確認
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(0)  # ノード0から探索

    return len(visited) == n
```

## 特殊なグラフ

### 1. 木 (Tree)

- 連結かつ非循環
- V個の頂点、V-1個の辺
- 任意の2頂点間にただ1つの経路

### 2. DAG (Directed Acyclic Graph / 有向非巡回グラフ)

- 有向かつ非循環
- トポロジカルソート（依存関係の順序付け）が可能
- 例: タスクの依存関係、履修順序

```python
def topological_sort(graph):
    """カーンのアルゴリズム"""
    in_degree = {v: 0 for v in graph}
    for v in graph:
        for neighbor in graph[v]:
            in_degree[neighbor] += 1

    queue = [v for v in in_degree if in_degree[v] == 0]
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == len(graph) else []  # サイクルがある場合は空リスト
```

### 3. 完全グラフ (Complete Graph)

- 全ての頂点対が辺で結ばれている
- V個の頂点でV(V-1)/2個の辺

### 4. 二部グラフ (Bipartite Graph)

- 頂点が2つのグループに分割可能
- 同じグループ内の頂点間に辺がない
- 例: マッチング問題（学生と企業、タスクと担当者）

```python
def is_bipartite(graph):
    """BFSで2色塗り分けを試みる"""
    color = {}

    for start in graph:
        if start in color:
            continue

        queue = [start]
        color[start] = 0

        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False  # 同じ色の隣接ノード

    return True
```

## グラフの基本操作

### 1. 頂点の追加・削除

```python
def add_vertex(graph, vertex):
    if vertex not in graph:
        graph[vertex] = []

def remove_vertex(graph, vertex):
    """頂点とそれに関連する全ての辺を削除"""
    if vertex in graph:
        # その頂点への辺を削除
        for v in graph:
            graph[v] = [edge for edge in graph[v] if edge[0] != vertex]
        # 頂点自体を削除
        del graph[vertex]
```

### 2. 辺の追加・削除

```python
def add_edge(graph, u, v, weight=1):
    """有向グラフにエッジを追加"""
    graph[u].append((v, weight))

def remove_edge(graph, u, v):
    """エッジを削除"""
    if u in graph:
        graph[u] = [edge for edge in graph[u] if edge[0] != v]
```

## 実装例: 重み付き有向グラフ

```python
from collections import defaultdict

class WeightedDirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v, weight):
        """エッジを追加"""
        self.graph[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)

    def get_weight(self, u, v):
        """u→vの重みを取得"""
        for neighbor, weight in self.graph[u]:
            if neighbor == v:
                return weight
        return float('inf')

    def get_vertices(self):
        """全ノードを取得"""
        return list(self.vertices)

    def get_edges(self):
        """全エッジを取得"""
        edges = []
        for u in self.graph:
            for v, weight in self.graph[u]:
                edges.append((u, v, weight))
        return edges

    def __repr__(self):
        """グラフの文字列表現"""
        result = []
        for u in sorted(self.graph.keys()):
            neighbors = ", ".join(f"{v}({w})" for v, w in self.graph[u])
            result.append(f"{u} -> [{neighbors}]")
        return "\n".join(result)


# 使用例
def main():
    g = WeightedDirectedGraph()

    # エッジを追加
    g.add_edge(0, 1, 5)  # A → B: 5
    g.add_edge(1, 2, 4)  # B → C: 4
    g.add_edge(1, 3, 9)  # B → D: 9
    g.add_edge(3, 0, 3)  # D → A: 3
    g.add_edge(3, 4, 2)  # D → E: 2

    print(g)
    print("\nVertices:", g.get_vertices())
    print("Edges:", g.get_edges())
    print("Weight 0→1:", g.get_weight(0, 1))

if __name__ == "__main__":
    main()
```

## まとめ

グラフは非常に汎用的なデータ構造で、多くの実世界の問題をモデル化できます。

### 重要なポイント

1. **4種類のグラフ**（無向/有向 × 重みなし/重みあり）を理解する
2. **隣接行列と隣接リスト**の使い分けを知る（LeetCodeでは主に隣接リスト）
3. **木はグラフの特殊ケース**（連結 + 閉路なし、エッジ数 = ノード数 - 1）
4. **グラフの性質**（連結性、閉路、次数）を把握する
5. **特殊なグラフ**（DAG、二部グラフなど）の特徴を知る
