"""
DFS (Depth-First Search / 深さ優先探索)

グラフの探索アルゴリズムの一つ。できるだけ深く探索してから、戻って別の経路を探索する。
スタック（または再帰）を使用して実装される。

特徴:
- 経路の存在確認、サイクル検出、トポロジカルソートなどに適している
- メモリ効率的（スタックの深さはO(h)、hは最大深さ）
- 空間計算量: O(h) - 再帰スタックの深さ、または明示的スタックのサイズ
- 時間計算量: O(V + E) - 全ノードと全エッジを探索
"""

from typing import List, Dict, Set, Optional


def dfs_recursive(
    graph: Dict[int, List[int]],
    start: int,
    visited: Optional[Set[int]] = None
) -> List[int]:
    """
    DFSの再帰実装（最も直感的な実装）

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード
        visited: 訪問済みノードの集合（内部使用）

    Returns:
        訪問順のノードリスト
    """
    if visited is None:
        visited = set()

    result = []
    visited.add(start)
    result.append(start)

    # 隣接ノードを再帰的に探索
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


def dfs_iterative(graph: Dict[int, List[int]], start: int) -> List[int]:
    """
    DFSの反復実装（スタックを使用）

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード

    Returns:
        訪問順のノードリスト
    """
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            result.append(node)

            # 隣接ノードをスタックに追加（逆順で追加すると再帰版と同じ順序になる）
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def dfs_with_path(
    graph: Dict[int, List[int]],
    start: int,
    goal: int,
    path: Optional[List[int]] = None
) -> Optional[List[int]]:
    """
    DFSを使った経路探索

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード
        goal: 目標ノード
        path: 現在の経路（内部使用）

    Returns:
        経路のリスト（見つからない場合はNone）
    """
    if path is None:
        path = []

    path = path + [start]

    if start == goal:
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in path:  # サイクル回避
            new_path = dfs_with_path(graph, neighbor, goal, path)
            if new_path:
                return new_path

    return None


def dfs_all_paths(
    graph: Dict[int, List[int]],
    start: int,
    goal: int,
    path: Optional[List[int]] = None
) -> List[List[int]]:
    """
    DFSを使ったすべての経路探索

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード
        goal: 目標ノード
        path: 現在の経路（内部使用）

    Returns:
        すべての経路のリスト
    """
    if path is None:
        path = []

    path = path + [start]

    if start == goal:
        return [path]

    paths = []
    for neighbor in graph.get(start, []):
        if neighbor not in path:
            new_paths = dfs_all_paths(graph, neighbor, goal, path)
            paths.extend(new_paths)

    return paths


def has_cycle_undirected(graph: Dict[int, List[int]]) -> bool:
    """
    無向グラフのサイクル検出（DFS使用）

    Args:
        graph: 隣接リストで表現されたグラフ

    Returns:
        サイクルが存在する場合True
    """
    visited = set()

    def dfs(node: int, parent: int) -> bool:
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                # 訪問済みで親でない → サイクル発見
                return True

        return False

    # すべての連結成分をチェック
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


def has_cycle_directed(graph: Dict[int, List[int]]) -> bool:
    """
    有向グラフのサイクル検出（DFS使用）

    Args:
        graph: 隣接リストで表現されたグラフ

    Returns:
        サイクルが存在する場合True
    """
    WHITE, GRAY, BLACK = 0, 1, 2  # 未訪問、訪問中、訪問完了
    color = {node: WHITE for node in graph}

    def dfs(node: int) -> bool:
        color[node] = GRAY  # 訪問中

        for neighbor in graph.get(node, []):
            if color.get(neighbor, WHITE) == GRAY:
                # 訪問中のノードに到達 → バックエッジ発見 → サイクル
                return True
            if color.get(neighbor, WHITE) == WHITE:
                if dfs(neighbor):
                    return True

        color[node] = BLACK  # 訪問完了
        return False

    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True

    return False


def topological_sort_dfs(graph: Dict[int, List[int]]) -> Optional[List[int]]:
    """
    DFSを使ったトポロジカルソート

    Args:
        graph: 隣接リストで表現された有向グラフ

    Returns:
        トポロジカル順序のリスト（サイクルがある場合はNone）
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    result = []

    def dfs(node: int) -> bool:
        color[node] = GRAY

        for neighbor in graph.get(node, []):
            if color.get(neighbor, WHITE) == GRAY:
                return False  # サイクル検出
            if color.get(neighbor, WHITE) == WHITE:
                if not dfs(neighbor):
                    return False

        color[node] = BLACK
        result.append(node)  # 後順走査で追加
        return True

    for node in graph:
        if color[node] == WHITE:
            if not dfs(node):
                return None  # サイクルがある

    return result[::-1]  # 逆順にして返す


def dfs_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    DFSを使った連結成分の検出

    Args:
        graph: 隣接リストで表現されたグラフ

    Returns:
        連結成分のリスト（各成分はノードのリスト）
    """
    visited = set()
    components = []

    def dfs(node: int, component: List[int]):
        visited.add(node)
        component.append(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, component)
            components.append(component)

    return components


def dfs_visualize(graph: Dict[int, List[int]], start: int) -> None:
    """
    DFSの探索過程を視覚的に表示（再帰版）

    Args:
        graph: 隣接リストで表現されたグラフ
        start: 開始ノード
    """
    visited = set()
    depth = [0]  # リストで包んで参照を保持

    def dfs(node: int):
        visited.add(node)
        indent = "  " * depth[0]
        print(f"{indent}訪問: ノード {node}")

        neighbors = [n for n in graph.get(node, []) if n not in visited]
        if neighbors:
            print(f"{indent}隣接ノード: {neighbors}")

        depth[0] += 1
        for neighbor in neighbors:
            dfs(neighbor)
        depth[0] -= 1

        if depth[0] == 0:
            print(f"{indent}← ノード {node} の探索完了")

    print(f"DFS探索開始: ノード {start}")
    print("=" * 50)
    dfs(start)
    print("=" * 50)
    print(f"探索完了。訪問したノード: {sorted(visited)}")


def main():
    """
    DFSのサンプル実行
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

    # 1. 再帰的DFS
    print("1. 再帰的DFS（ノード0から開始）:")
    result = dfs_recursive(graph, 0)
    print(f"   訪問順: {result}")
    print()

    # 2. 反復的DFS
    print("2. 反復的DFS（スタック使用）:")
    result = dfs_iterative(graph, 0)
    print(f"   訪問順: {result}")
    print()

    # 3. 経路探索
    print("3. 経路探索（0 → 5）:")
    path = dfs_with_path(graph, 0, 5)
    if path:
        print(f"   経路: {' → '.join(map(str, path))}")
    print()

    # 4. すべての経路探索
    print("4. すべての経路探索（0 → 5）:")
    all_paths = dfs_all_paths(graph, 0, 5)
    for i, path in enumerate(all_paths, 1):
        print(f"   経路 {i}: {' → '.join(map(str, path))}")
    print()

    # 5. サイクル検出（無向グラフ）
    print("5. サイクル検出（無向グラフ）:")
    has_cycle = has_cycle_undirected(graph)
    print(f"   サイクルあり: {has_cycle}")
    print()

    # 6. サイクル検出（有向グラフ）
    directed_graph = {
        0: [1],
        1: [2],
        2: [3],
        3: [1],  # サイクル: 1 → 2 → 3 → 1
    }
    print("6. サイクル検出（有向グラフ）:")
    has_cycle = has_cycle_directed(directed_graph)
    print(f"   サイクルあり: {has_cycle}")
    print()

    # 7. トポロジカルソート
    dag = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: [],
    }
    print("7. トポロジカルソート（DAG）:")
    topo_order = topological_sort_dfs(dag)
    print(f"   順序: {topo_order}")
    print()

    # 8. 連結成分の検出
    disconnected_graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2],
        4: [5],
        5: [4],
    }
    print("8. 連結成分の検出（非連結グラフ）:")
    components = dfs_connected_components(disconnected_graph)
    for i, component in enumerate(components, 1):
        print(f"   成分 {i}: {sorted(component)}")
    print()

    # 9. DFS探索過程の視覚化
    print("9. DFS探索過程の視覚化:")
    dfs_visualize(graph, 0)


if __name__ == "__main__":
    main()
