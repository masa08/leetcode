from typing import List


def main():
    solution = Solution()

    # Basic cases
    m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    solution.setZeroes(m1)
    assert m1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution.setZeroes(m2)
    assert m2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    # Edge cases
    m3 = [[1]]
    solution.setZeroes(m3)
    assert m3 == [[1]]

    m4 = [[0]]
    solution.setZeroes(m4)
    assert m4 == [[0]]

    print("All tests passed!")


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Two-pass: first pass records which rows and cols contain 0,
        second pass sets those rows and cols to 0.

        Time: O(m*n) - two passes through the matrix
        Space: O(m+n) - sets to store zero rows and cols
        """
        zero_rows = set()
        zero_cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0


if __name__ == '__main__':
    main()
