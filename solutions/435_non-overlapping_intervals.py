from typing import List
from math import inf


def main():
    args = [[1, 2], [2, 3], [3, 4], [1, 3]]
    solution = Solution()
    result = solution.eraseOverlapIntervals(args)
    print(result)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        count = 0
        k = -inf

        for start, end in intervals:
            if start >= k:
                k = end
            else:
                count += 1

        return count


if __name__ == '__main__':
    main()
