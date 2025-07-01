# 2D配列の行列変換（問題2352パターン）

# 基本: 行と列の抽出
def extract_row_as_tuple(grid, row_idx):
    """行をタプルとして抽出"""
    return tuple(grid[row_idx])


def extract_column_as_tuple(grid, col_idx):
    """列をタプルとして抽出"""
    return tuple(grid[i][col_idx] for i in range(len(grid)))

# ハッシュテーブル + カウンティング


def frequency_counting_approach(grid):
    """問題2352の解法パターン"""
    n = len(grid)
    count = 0
    row_counter = {}

    # 行をカウント
    for i in range(n):
        row_tuple = tuple(grid[i])
        row_counter[row_tuple] = row_counter.get(row_tuple, 0) + 1

    # 列と比較
    for j in range(n):
        col_tuple = tuple(grid[i][j] for i in range(n))
        count += row_counter.get(col_tuple, 0)

    return count

# 重要ポイント:
# - tuple使用（ハッシュ可能）
# - dict.get()でデフォルト値
# - 時間計算量: O(n²)
