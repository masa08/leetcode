from collections import deque
from typing import List


def main():
    numCourses = 2
    prerequisites = [[1, 0]]
    solution = Solution()
    result = solution.canFinish(numCourses, prerequisites)
    print(result)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Kahn's Algorithm (BFS ベースのトポロジカルソート) で循環検出する
        - indegree(入次数) = 0 のノードから順に処理していく
        - 全ノードを処理できれば循環なし → True
        - 処理できないノードが残れば循環あり → False
        Time: O(V + E)
          - グラフ構築: prerequisites を1回ループ → O(E)
          - indegree=0 探索: 全ノードを1回ループ → O(V)
          - BFS: while が最大 V 回、内側 for は全ノード合計で E 回 → O(V + E)
        Space: O(V + E)
          - graph: V 個のリスト + 中身は全エッジ E 個 → O(V + E)
          - indegree: V 個 → O(V)
          - queue: 最大 V 個 → O(V)
        """
        # グラフの構築と各ノードの入次数を計算
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # 入次数0（前提条件なし）のノードをキューに入れる
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # BFS で処理: 取り出したノードの先にあるノードの入次数を減らす
        count = 0
        while queue:
            current = queue.popleft()
            count += 1

            for next_course in graph[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # 全コースを処理できたか = 循環がないか
        return count == numCourses


if __name__ == '__main__':
    main()
