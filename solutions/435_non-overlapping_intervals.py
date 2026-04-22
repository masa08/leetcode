from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.eraseOverlapIntervals(
        [[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2

    # Edge cases
    assert solution.eraseOverlapIntervals(
        [[1, 2]]) == 0           # Single interval
    assert solution.eraseOverlapIntervals([[1, 2], [3, 4]]) == 0   # No overlap
    assert solution.eraseOverlapIntervals([[1, 3], [2, 4], [3, 5]]) == 1

    print("All tests passed!")


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Greedy: sort by start, then compare each interval with prev_end.
        If overlapping, remove the one with the larger end (keep min) to
        minimize future overlaps. Count each removal.

        Time: O(n log n) - sorting dominates
        Space: O(1) - only tracking prev_end and count
        """
        intervals.sort(key=lambda x: x[0])
        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                count += 1
                prev_end = min(prev_end, intervals[i][1])
            else:
                prev_end = intervals[i][1]

        return count


if __name__ == '__main__':
    main()
