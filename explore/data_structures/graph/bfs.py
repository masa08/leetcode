"""
BFS (Breadth-First Search / 幅優先探索)

グラフの探索アルゴリズムの一つ。開始ノードから近い順に探索していく。
キューを使用して実装される。

特徴:
- 最短経路を見つけるのに適している（無重みグラフの場合）
- レベルごとに探索（層ごとに探索）
- 空間計算量: O(V) - キューに最大O(V)個のノードを保存
- 時間計算量: O(V + E) - 全ノードと全エッジを探索
"""

from collections import deque
from typing import List, Dict, Set


def bfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    BFSの反復実装（標準的な実装）

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード

    Returns:
        訪問順のノードリスト
    """
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        result.append(node)

        # 隣接ノードをキューに追加
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_with_level(graph: Dict[int, List[int]], start: int) -> Dict[int, int]:
    """
    レベル（深さ）情報付きBFS
    各ノードが開始ノードから何ステップ離れているかを記録

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード

    Returns:
        {ノード: レベル} の辞書
    """
    visited = {start}
    queue = deque([(start, 0)])  # (ノード, レベル)
    levels = {start: 0}

    while queue:
        node, level = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                levels[neighbor] = level + 1
                queue.append((neighbor, level + 1))

    return levels


def bfs_shortest_path(graph: Dict[int, List[int]], start: int, goal: int) -> List[int]:
    """
    BFSを使った最短経路探索（無重みグラフ）

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード
        goal: 目標ノード

    Returns:
        最短経路のノードリスト（見つからない場合は空リスト）
    """
    if start == goal:
        return [start]

    visited = {start}
    queue = deque([(start, [start])])  # (現在のノード, 経路)

    while queue:
        node, path = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == goal:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return []  # 経路が見つからない


def bfs_all_paths_at_distance(
    graph: Dict[int, List[int]],
    start: int,
    distance: int
) -> List[int]:
    """
    開始ノードから指定距離にあるすべてのノードを取得

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード
        distance: 距離

    Returns:
        指定距離にあるノードのリスト
    """
    visited = {start}
    queue = deque([(start, 0)])
    nodes_at_distance = []

    while queue:
        node, level = queue.popleft()

        if level == distance:
            nodes_at_distance.append(node)
            continue  # これ以上探索しない

        if level < distance:
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

    return nodes_at_distance


def bfs_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    BFSを使った連結成分の検出

    Args:
        graph: 隣接リストで表現されたグラフ

    Returns:
        連結成分のリスト（各成分はノードのリスト）
    """
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            # 新しい連結成分を発見
            component = []
            queue = deque([node])
            visited.add(node)

            while queue:
                current = queue.popleft()
                component.append(current)

                for neighbor in graph.get(current, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components.append(component)

    return components


def bfs_visualize(graph: Dict[int, List[int]], start: int) -> None:
    """
    BFSの探索過程を視覚的に表示

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    level = 0

    print(f"BFS探索開始: ノード {start}")
    print("=" * 50)

    while queue:
        level_size = len(queue)
        print(f"\nレベル {level}:")
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node)

            # 隣接ノードをキューに追加
            neighbors = []
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    neighbors.append(neighbor)

            if neighbors:
                print(f"  ノード {node} → 隣接ノード {neighbors} をキューに追加")
            else:
                print(f"  ノード {node} → 新しい隣接ノードなし")

        print(f"  訪問: {level_nodes}")
        level += 1

    print("\n" + "=" * 50)
    print(f"探索完了。訪問したノード: {sorted(visited)}")


def main():
    """
    BFSのサンプル実行
    """
    # サンプルグラフ（無向グラフ）
    #     0 --- 1
    #     |     |
    #     2 --- 3 --- 4
    #           |
    #           5
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4, 5],
        4: [3],
        5: [3],
    }

    print("グラフ構造:")
    print("    0 --- 1")
    print("    |     |")
    print("    2 --- 3 --- 4")
    print("          |")
    print("          5")
    print()

    # 1. 基本的なBFS
    print("1. 基本的なBFS（ノード0から開始）:")
    result = bfs_iterative(graph, 0)
    print(f"   訪問順: {result}")
    print()

    # 2. レベル情報付きBFS
    print("2. レベル情報付きBFS:")
    levels = bfs_with_level(graph, 0)
    for node in sorted(levels.keys()):
        print(f"   ノード {node}: レベル {levels[node]}")
    print()

    # 3. 最短経路探索
    print("3. 最短経路探索（0 → 5）:")
    path = bfs_shortest_path(graph, 0, 5)
    print(f"   最短経路: {' → '.join(map(str, path))}")
    print(f"   距離: {len(path) - 1}")
    print()

    # 4. 指定距離のノード取得
    print("4. ノード0から距離2のノード:")
    nodes = bfs_all_paths_at_distance(graph, 0, 2)
    print(f"   ノード: {sorted(nodes)}")
    print()

    # 5. 連結成分の検出
    disconnected_graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2],
        4: [5],
        5: [4],
    }
    print("5. 連結成分の検出（非連結グラフ）:")
    components = bfs_connected_components(disconnected_graph)
    for i, component in enumerate(components, 1):
        print(f"   成分 {i}: {sorted(component)}")
    print()

    # 6. BFS探索過程の視覚化
    print("6. BFS探索過程の視覚化:")
    bfs_visualize(graph, 0)


if __name__ == "__main__":
    main()
