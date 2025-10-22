from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert newInterval into intervals and merge overlapping intervals.

        Approach:
        1. Add all intervals that come before newInterval
        2. Merge all overlapping intervals with newInterval
        3. Add all intervals that come after newInterval

        Time: O(n) - single pass through intervals
        Space: O(n) - result list
        """
        # Edge cases
        if not intervals:
            return [newInterval]

        result = []
        i = 0
        n = len(intervals)

        # 1. Add all intervals that come before newInterval (no overlap)
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. Merge all overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # 3. Add all intervals that come after newInterval (no overlap)
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


def main():
    solution = Solution()

    # Test case 1: Basic merge
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    assert solution.insert(intervals1, newInterval1) == [[1, 5], [6, 9]]

    # Test case 2: Multiple merges
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    assert solution.insert(intervals2, newInterval2) == [
        [1, 2], [3, 10], [12, 16]]

    # Test case 3: No overlap, insert at beginning
    intervals3 = [[3, 5], [6, 9]]
    newInterval3 = [1, 2]
    assert solution.insert(intervals3, newInterval3) == [
        [1, 2], [3, 5], [6, 9]]

    # Test case 4: No overlap, insert at end
    intervals4 = [[1, 3], [6, 9]]
    newInterval4 = [10, 12]
    assert solution.insert(intervals4, newInterval4) == [
        [1, 3], [6, 9], [10, 12]]

    # Test case 5: Empty intervals
    intervals5 = []
    newInterval5 = [5, 7]
    assert solution.insert(intervals5, newInterval5) == [[5, 7]]

    # Test case 6: New interval covers all existing intervals
    intervals6 = [[1, 2], [3, 5], [6, 7]]
    newInterval6 = [0, 10]
    assert solution.insert(intervals6, newInterval6) == [[0, 10]]

    # Test case 7: New interval inside existing interval
    intervals7 = [[1, 5]]
    newInterval7 = [2, 3]
    assert solution.insert(intervals7, newInterval7) == [[1, 5]]

    print("All tests passed!")


if __name__ == "__main__":
    main()
