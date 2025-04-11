from typing import List
from math import inf


def main():
    args = [[1, 2], [2, 3], [3, 4], [1, 3]]
    solution = Solution()
    result = solution.eraseOverlapIntervals(args)
    print(result)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[1])
        count = 0
        latest_end = -inf

        for start, end in intervals:
            if start >= latest_end:
                latest_end = end
            else:
                count += 1

        return count


if __name__ == '__main__':
    main()
