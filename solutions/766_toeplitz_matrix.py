from typing import List


def main():
    args = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    solution = Solution()
    result = solution.isToeplitzMatrix(args)
    print(result)


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        notInvalid = []

        def _dfs(r, c, val):
            if (r < 0 or c < 0 or r >= len(matrix) or c >= len(matrix[0])):
                return
            if (val != matrix[r][c]):
                notInvalid.append([r, c])
            _dfs(r+1, c+1, val)

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                _dfs(row, column, matrix[row][column])

        return not notInvalid

        # for ri in range(1, len(matrix)):
        #     for ci in range(1, len(matrix[ri])):
        #         if matrix[ri][ci] != matrix[ri-1][ci-1]:
        #             return False

        # return True


if __name__ == '__main__':
    main()
