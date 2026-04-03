from collections import deque
from typing import List


def main():
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    solution = Solution()
    result = solution.findOrder(numCourses, prerequisites)
    print(result)


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # numCourses: 4, prereq = [[1,0], [2,0], [3,1], [3,2]]
        # 0 -> 1 -> 3
        # ↓         ↑
        # 2 -> -> ->↑
        # graph = [[1, 2], [3], [3], []]
        # need_to_take = [0, 1, 1, 2]
        # queue = [0]: queueで受講可能な科目を追加、管理する
        # その後、queueから科目を取り出し、その科目を受講可能な科目をqueueに追加する
        # これを繰り返し、queueが空になるまで繰り返す

        graph = [[] for i in range(numCourses)]
        need_to_take = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            need_to_take[course] += 1

        queue = deque()
        for i in range(numCourses):
            if need_to_take[i] == 0:
                queue.append(i)

        count = 0
        result = []
        while queue:
            current = queue.popleft()
            result.append(current)
            next_courses = graph[current]
            for nc in next_courses:
                need_to_take[nc] -= 1
                if need_to_take[nc] == 0:
                    queue.append(nc)
            count += 1

        return result if count == numCourses else []


if __name__ == '__main__':
    main()
