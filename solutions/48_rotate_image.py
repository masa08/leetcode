from typing import List


def main():
    solution = Solution()

    # 基本ケース: 3x3
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Before: {matrix1}")
    solution.rotate(matrix1)
    print(f"After:  {matrix1}")
    assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    # 基本ケース: 4x4
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    solution.rotate(matrix2)
    assert matrix2 == [[15, 13, 2, 5], [
        14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    # エッジケース: 1x1
    matrix3 = [[1]]
    solution.rotate(matrix3)
    assert matrix3 == [[1]]

    # エッジケース: 2x2
    matrix4 = [[1, 2], [3, 4]]
    solution.rotate(matrix4)
    assert matrix4 == [[3, 1], [4, 2]]

    print("All tests passed!")


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        アプローチ1: レイヤーごとの4要素回転
        - 外側から内側へレイヤーごとに処理
        - 各位置で4つの要素を循環的に移動
        - 時間: O(n²), 空間: O(1)
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                # 一時変数に現在の値を保存
                tmp = matrix[i][j]
                # 左下から左上へ値を移動
                matrix[i][j] = matrix[n-j-1][i]
                # 右下から左下へ値を移動
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                # 右上から右下へ値を移動
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                # 一時変数から右上へ値を移動
                matrix[j][n-i-1] = tmp

    def rotate_v2(self, matrix: List[List[int]]) -> None:
        """
        アプローチ2: 転置＋反転（より直感的）

        Step 1: 転置（行と列を入れ替え）
        [1,2,3]     [1,4,7]
        [4,5,6] =>  [2,5,8]
        [7,8,9]     [3,6,9]

        Step 2: 各行を左右反転
        [1,4,7]     [7,4,1]
        [2,5,8] =>  [8,5,2]
        [3,6,9]     [9,6,3]

        時間: O(n²), 空間: O(1)
        """
        n = len(matrix)

        # Step 1: 転置（対角線で対称に入れ替え）
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: 各行を左右反転
        for i in range(n):
            matrix[i].reverse()
            # または: matrix[i] = matrix[i][::-1]


if __name__ == '__main__':
    main()
