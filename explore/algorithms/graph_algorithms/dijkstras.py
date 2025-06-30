import heapq


def main():
    graph = [
        [None, 2, 5, None, None, None],
        [2, None, 4, 6, 10, None],
        [5, 4, None, 2, None, None],
        [None, 6, 2, None, None, 1],
        [None, 10, None, None, None, 3],
        [None, None, None, 1, 3, None],
    ]
    start_vertex = 0

    solution = Solution()
    dist = solution.dijkstra(graph, start_vertex)

    print(dist)


class Solution:
    def dijkstra(self, graph, start_vertex):
        VERTEX_COUNT = len(graph)
        dist_from_start = [float('inf')] * VERTEX_COUNT
        dist_from_start[start_vertex] = 0

        queue = [(0, start_vertex)]
        while queue:
            vertex_dist, vertex = heapq.heappop(queue)

            # vertexへの距離が最小でない場合はスキップする
            if dist_from_start[vertex] < vertex_dist:
                continue

            for next_v, edge_cost in enumerate(graph[vertex]):
                if edge_cost is not None and vertex_dist + edge_cost < dist_from_start[next_v]:
                    dist_from_start[next_v] = vertex_dist + edge_cost
                    heapq.heappush(queue, (dist_from_start[next_v], next_v))

        return dist_from_start


if __name__ == '__main__':
    main()
