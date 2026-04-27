import heapq
from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert solution.minMeetingRooms([[7, 10], [2, 4]]) == 1

    # Edge cases
    assert solution.minMeetingRooms(
        []) == 0                         # No meetings
    assert solution.minMeetingRooms(
        [[1, 5]]) == 1                   # Single meeting
    assert solution.minMeetingRooms(
        [[1, 5], [5, 10]]) == 1          # Touching ends
    assert solution.minMeetingRooms(
        [[1, 5], [2, 6], [3, 7]]) == 3   # All overlap

    print("All tests passed!")


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Min-heap of room end times.
        Sort intervals by start. For each meeting:
          - If the earliest-ending room is free (heap[0] <= start), reuse it.
          - Otherwise, allocate a new room.
        The heap size at the end equals the max number of concurrent rooms.

        Time: O(n log n) - sorting + heap operations
        Space: O(n) - heap stores up to n end times
        """
        intervals.sort(key=lambda x: x[0])
        heap = []

        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)


if __name__ == '__main__':
    main()
