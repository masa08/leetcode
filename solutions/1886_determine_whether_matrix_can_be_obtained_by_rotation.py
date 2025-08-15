from typing import List


def main():
    s = Solution()
    print(s.findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]))  # True
    print(s.findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]))  # False


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        # 2D配列の回転変換公式
        # 元の位置: mat[i][j]
        # 90度回転:  mat[i][j] → [j][n-1-i]
        # 180度回転: mat[i][j] → [n-1-i][n-1-j]
        # 270度回転: mat[i][j] → [n-1-j][i]
        all_rotations = [True] * 4
        for row in range(n):
            for col in range(n):
                if mat[row][col] != target[col][n-row-1]:
                    all_rotations[0] = False
                if mat[row][col] != target[n-row-1][n-col-1]:
                    all_rotations[1] = False
                if mat[row][col] != target[n-col-1][row]:
                    all_rotations[2] = False
                if mat[row][col] != target[row][col]:
                    all_rotations[3] = False

        return any(all_rotations)


if __name__ == '__main__':
    main()
