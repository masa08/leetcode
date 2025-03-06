from cmath import inf
from typing import List


def main():
    args = [[10, 16], [2, 8], [1, 6], [7, 12]]
    solution = Solution()
    result = solution.findMinArrowShots(args)
    print(result)


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        count = 0
        k = -inf

        for start, end in points:
            if start > k:
                k = end
                count += 1

        return count


if __name__ == '__main__':
    main()
