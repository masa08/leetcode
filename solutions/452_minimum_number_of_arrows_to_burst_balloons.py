from cmath import inf
from typing import List


def main():
    args = [[10, 16], [2, 8], [1, 6], [7, 12]]
    solution = Solution()
    result = solution.findMinArrowShots(args)
    print(result)


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        latest_end = -inf
        count = 0

        for start, end in points:
            if start > latest_end:
                latest_end = end
                count += 1

        return count


if __name__ == '__main__':
    main()
