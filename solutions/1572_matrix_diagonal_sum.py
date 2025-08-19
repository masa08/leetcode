from typing import List


def main():
    solution = Solution()

    # Test case 1: 3x3 matrix
    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    assert solution.diagonalSum(mat1) == 25

    # Test case 2: 4x4 matrix (even size)
    mat2 = [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]
    assert solution.diagonalSum(mat2) == 8

    # Test case 3: 1x1 matrix (edge case)
    mat3 = [[5]]
    assert solution.diagonalSum(mat3) == 5

    print("All tests passed!")


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_sum = 0
        n = len(mat)

        for i in range(n):
            diagonal_sum += mat[i][i]
            diagonal_sum += mat[i][n-i-1]

        if len(mat) % 2 == 1:
            diagonal_sum -= mat[n//2][n//2]

        return diagonal_sum


if __name__ == '__main__':
    main()
