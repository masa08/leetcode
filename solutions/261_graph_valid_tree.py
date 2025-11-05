from collections import defaultdict
from typing import List


def main():
    solution = Solution()

    # Valid tree
    assert solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True

    # Contains cycle
    assert solution.validTree(
        5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False

    # Not connected
    assert solution.validTree(4, [[0, 1], [2, 3]]) == False

    print("All tests passed!")


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Algorithm: DFS-based cycle detection and connectivity check
        - Valid tree must have exactly n-1 edges
        - Valid tree must be connected (all nodes reachable)
        - Valid tree must be acyclic (no cycles)

        Time Complexity: O(n + e) where e = number of edges
        Space Complexity: O(n + e) for graph adjacency list and visited set
        """
        # A valid tree with n nodes must have exactly n-1 edges
        if not self._hasValidEdgeCount(n, edges):
            return False

        # Build adjacency list representation
        graph = self._buildGraph(edges)

        # Check if graph is acyclic and fully connected
        visited = set()
        has_cycle = self._detectCycle(graph, visited, start_node=0, parent=-1)
        is_fully_connected = len(visited) == n

        return not has_cycle and is_fully_connected

    def _hasValidEdgeCount(self, n: int, edges: List[List[int]]) -> bool:
        """A tree with n nodes must have exactly n-1 edges"""
        return len(edges) == n - 1

    def _buildGraph(self, edges: List[List[int]]) -> defaultdict:
        """Build undirected graph as adjacency list"""
        graph = defaultdict(list)
        for node_a, node_b in edges:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)
        return graph

    def _detectCycle(self, graph: defaultdict, visited: set, start_node: int, parent: int) -> bool:
        """DFS to detect cycle in undirected graph"""
        # If we visit a node twice, there's a cycle
        if start_node in visited:
            return True

        visited.add(start_node)

        # Check all neighbors
        for neighbor in graph[start_node]:
            # Skip the parent to avoid false cycle detection in undirected graph
            if neighbor == parent:
                continue

            # Recursively check neighbor
            if self._detectCycle(graph, visited, neighbor, start_node):
                return True

        return False


if __name__ == '__main__':
    main()
