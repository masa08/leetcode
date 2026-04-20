from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]

    # Edge cases
    assert solution.merge([[1, 4]]) == [[1, 4]]             # Single interval
    assert solution.merge([[1, 4], [5, 6]]) == [[1, 4], [5, 6]]  # No overlap
    assert solution.merge([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]  # All contained

    print("All tests passed!")


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort by start, then iterate and merge overlapping intervals.
        Compare each interval with the last one in result — if they overlap,
        extend the end; otherwise, add as a new interval.

        Time: O(n log n) - sorting dominates
        Space: O(n) - result array
        """
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

        return result


if __name__ == '__main__':
    main()
