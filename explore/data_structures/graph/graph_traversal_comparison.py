"""
グラフ探索アルゴリズムの比較: BFS vs DFS

BFSとDFSの動作の違いを視覚的に比較し、
それぞれがどのような問題に適しているかを理解する。
"""

from collections import deque
from typing import List, Dict, Tuple


def bfs_with_trace(graph: Dict[int, List[int]], start: int) -> List[Tuple[int, int]]:
    """
    BFSの探索順序をトレース

    Returns:
        [(ノード, レベル), ...] のリスト
    """
    visited = {start}
    queue = deque([(start, 0)])
    trace = []

    while queue:
        node, level = queue.popleft()
        trace.append((node, level))

        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))

    return trace


def dfs_with_trace(
    graph: Dict[int, List[int]],
    start: int,
    visited: set = None,
    depth: int = 0,
    trace: List[Tuple[int, int]] = None
) -> List[Tuple[int, int]]:
    """
    DFSの探索順序をトレース

    Returns:
        [(ノード, 深さ), ...] のリスト
    """
    if visited is None:
        visited = set()
    if trace is None:
        trace = []

    visited.add(start)
    trace.append((start, depth))

    for neighbor in sorted(graph.get(start, [])):
        if neighbor not in visited:
            dfs_with_trace(graph, neighbor, visited, depth + 1, trace)

    return trace


def visualize_comparison(graph: Dict[int, List[int]], start: int) -> None:
    """
    BFSとDFSの探索順序を並べて比較表示
    """
    print("=" * 80)
    print(f"グラフ探索の比較: 開始ノード {start}")
    print("=" * 80)
    print()

    # BFSの探索
    print("【BFS: 幅優先探索】")
    print("特徴: 近いノードから順に探索（レベルごと）")
    print("-" * 40)
    bfs_trace = bfs_with_trace(graph, start)
    for i, (node, level) in enumerate(bfs_trace, 1):
        print(f"  {i:2d}. ノード {node} (レベル {level})")
    print()

    # DFSの探索
    print("【DFS: 深さ優先探索】")
    print("特徴: できるだけ深く探索してから戻る")
    print("-" * 40)
    dfs_trace = dfs_with_trace(graph, start)
    for i, (node, depth) in enumerate(dfs_trace, 1):
        print(f"  {i:2d}. ノード {node} (深さ {depth})")
    print()

    # 違いの分析
    print("【探索順序の違い】")
    print("-" * 40)
    print("訪問順:")
    bfs_order = [node for node, _ in bfs_trace]
    dfs_order = [node for node, _ in dfs_trace]
    print(f"  BFS: {' → '.join(map(str, bfs_order))}")
    print(f"  DFS: {' → '.join(map(str, dfs_order))}")
    print()


def compare_shortest_path(graph: Dict[int, List[int]], start: int, goal: int) -> None:
    """
    最短経路探索における BFS と DFS の比較
    """
    print("=" * 80)
    print(f"最短経路探索: {start} → {goal}")
    print("=" * 80)
    print()

    # BFS: 最短経路を見つける（無重みグラフ）
    def bfs_shortest_path():
        if start == goal:
            return [start]

        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()

            for neighbor in graph.get(node, []):
                if neighbor == goal:
                    return path + [neighbor]

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    # DFS: 経路を見つける（最短とは限らない）
    def dfs_find_path(node=start, path=None):
        if path is None:
            path = []
        path = path + [node]

        if node == goal:
            return path

        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in path:
                result = dfs_find_path(neighbor, path)
                if result:
                    return result

        return None

    bfs_path = bfs_shortest_path()
    dfs_path = dfs_find_path()

    print("【BFSによる経路探索】")
    if bfs_path:
        print(f"  経路: {' → '.join(map(str, bfs_path))}")
        print(f"  距離: {len(bfs_path) - 1}")
        print(f"  ✓ 保証: 最短経路")
    else:
        print("  経路なし")
    print()

    print("【DFSによる経路探索】")
    if dfs_path:
        print(f"  経路: {' → '.join(map(str, dfs_path))}")
        print(f"  距離: {len(dfs_path) - 1}")
        if dfs_path == bfs_path:
            print(f"  ✓ この場合は最短経路と一致")
        else:
            print(f"  ! 最短経路とは限らない")
    else:
        print("  経路なし")
    print()


def use_case_examples():
    """
    BFSとDFSの使い分けの具体例
    """
    print("=" * 80)
    print("BFS と DFS の使い分け")
    print("=" * 80)
    print()

    print("【BFSが適している場合】")
    print("-" * 40)
    print("1. 最短経路探索（無重みグラフ）")
    print("   例: 迷路の最短経路、SNSの最短つながり")
    print()
    print("2. レベルごとの処理")
    print("   例: 木の幅優先走査、階層的な構造の処理")
    print()
    print("3. 目標が近いことがわかっている場合")
    print("   例: チェスの最短手数、近隣探索")
    print()

    print("【DFSが適している場合】")
    print("-" * 40)
    print("1. 経路の存在確認（最短でなくてもよい）")
    print("   例: 迷路の出口探索、グラフの到達可能性")
    print()
    print("2. サイクル検出")
    print("   例: 循環参照の検出、デッドロック検出")
    print()
    print("3. トポロジカルソート")
    print("   例: タスクの依存関係解決、ビルドシステム")
    print()
    print("4. すべての経路を列挙")
    print("   例: 組み合わせ問題、バックトラッキング")
    print()
    print("5. メモリ使用量を抑えたい場合")
    print("   例: 深い木構造の探索")
    print()


def complexity_comparison():
    """
    計算量の比較
    """
    print("=" * 80)
    print("計算量の比較")
    print("=" * 80)
    print()

    comparison = [
        ("時間計算量", "O(V + E)", "O(V + E)", "同じ（全ノード・全エッジを訪問）"),
        ("空間計算量", "O(V)", "O(h)", "BFSの方が多い（h: 最大深さ）"),
        ("キュー/スタック", "O(V)", "O(h)", "BFSは最悪O(V)、DFSは深さに依存"),
        ("最短経路保証", "◯", "✕", "BFSのみ保証（無重みグラフ）"),
        ("実装の簡潔さ", "反復", "再帰/反復", "DFSは再帰で簡潔に書ける"),
    ]

    print(f"{'項目':<15} {'BFS':<12} {'DFS':<12} {'備考'}")
    print("-" * 80)
    for item, bfs, dfs, note in comparison:
        print(f"{item:<15} {bfs:<12} {dfs:<12} {note}")
    print()


def main():
    """
    サンプル実行: 複数のグラフでBFSとDFSを比較
    """
    # サンプルグラフ1: 単純な無向グラフ
    print("グラフ1: 単純な無向グラフ")
    print("    0 --- 1")
    print("    |     |")
    print("    2 --- 3 --- 4")
    print("          |")
    print("          5")
    print()

    graph1 = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4, 5],
        4: [3],
        5: [3],
    }

    visualize_comparison(graph1, 0)
    compare_shortest_path(graph1, 0, 5)

    # サンプルグラフ2: 線形グラフ
    print("\n" + "=" * 80)
    print("グラフ2: 線形グラフ（一本道）")
    print("    0 --- 1 --- 2 --- 3 --- 4")
    print()

    graph2 = {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [3],
    }

    visualize_comparison(graph2, 0)

    # サンプルグラフ3: 木構造
    print("\n" + "=" * 80)
    print("グラフ3: 木構造（二分木）")
    print("        0")
    print("       / \\")
    print("      1   2")
    print("     / \\ / \\")
    print("    3  4 5  6")
    print()

    graph3 = {
        0: [1, 2],
        1: [3, 4],
        2: [5, 6],
        3: [],
        4: [],
        5: [],
        6: [],
    }

    visualize_comparison(graph3, 0)

    # 使い分けの説明
    use_case_examples()

    # 計算量の比較
    complexity_comparison()

    print("=" * 80)
    print("まとめ")
    print("=" * 80)
    print()
    print("• BFS: 最短経路を求める、レベルごとに処理する場合に使用")
    print("• DFS: 経路の存在確認、サイクル検出、トポロジカルソートに使用")
    print("• 問題の性質に応じて適切なアルゴリズムを選択することが重要")
    print()


if __name__ == "__main__":
    main()
