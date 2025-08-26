from typing import List


def main():
    solution = Solution()

    # 基本ケース
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert solution.spiralOrder(matrix1) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # 単一行
    matrix2 = [[1, 2, 3, 4]]
    assert solution.spiralOrder(matrix2) == [1, 2, 3, 4]

    # 単一列
    matrix3 = [[1], [2], [3]]
    assert solution.spiralOrder(matrix3) == [1, 2, 3]

    print("All tests passed!")


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        elems = []  # 結果を格納するリスト
        rows, cols = len(matrix), len(matrix[0])  # 行数と列数
        top, bottom, left, right = 0, rows - 1, 0, cols - 1  # 上、下、左、右の境界

        # 上と下の境界、左と右の境界が交差しない限りループ
        while top <= bottom and left <= right:
            for col in range(left, right+1):
                # 上の境界の要素を追加
                elems.append(matrix[top][col])

            for row in range(top+1, bottom+1):
                # 右の境界の要素を追加
                elems.append(matrix[row][right])

            # 境界が一行しかない場合はここには入らない
            if top != bottom:
                for col in reversed(range(left, right)):
                    # 下の境界の要素を追加
                    elems.append(matrix[bottom][col])

            # 境界が一列しかない場合はここには入らない
            if left != right:
                for row in reversed(range(top+1, bottom)):
                    # 左の境界の要素を追加
                    elems.append(matrix[row][left])

            # 上、下、左、右の境界を狭める
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return elems


if __name__ == '__main__':
    main()
