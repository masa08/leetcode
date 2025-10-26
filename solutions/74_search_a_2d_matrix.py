from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Two-step binary search approach with separation of concerns:
        1. Find the potential row (helper method)
        2. Search within that row (helper method)

        Time: log(m * n)
        Space: O(1)
        """
        # Edge cases
        if not matrix or not matrix[0]:
            return False

        # Step 1: Find the row that might contain target
        row = self._find_target_row(matrix, target)
        if row == -1:
            return False

        # Step 2: Search within the row
        return self._binary_search_in_row(matrix[row], target)

    def _find_target_row(self, matrix: List[List[int]], target: int) -> int:
        """
        Find the row where matrix[row][0] <= target <= matrix[row][-1]

        Returns:
            Row index if found, -1 otherwise
        """
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return mid
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1

        return -1

    def _binary_search_in_row(self, row: List[int], target: int) -> bool:
        """
        Standard binary search within a sorted array

        Returns:
            True if target found, False otherwise
        """
        left, right = 0, len(row) - 1

        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


def main():
    solution = Solution()

    # Basic cases
    assert solution.searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
    assert solution.searchMatrix(
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False

    # Edge cases: single element
    assert solution.searchMatrix([[1]], 1) == True
    assert solution.searchMatrix([[1]], 2) == False

    # Edge case: single row
    assert solution.searchMatrix([[1, 3, 5, 7]], 5) == True
    assert solution.searchMatrix([[1, 3, 5, 7]], 6) == False

    # Edge case: single column
    assert solution.searchMatrix([[1], [3], [5]], 3) == True
    assert solution.searchMatrix([[1], [3], [5]], 4) == False

    # Target at boundaries
    assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20]], 1) == True
    assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20]], 20) == True

    print("All tests passed!")


if __name__ == "__main__":
    main()
