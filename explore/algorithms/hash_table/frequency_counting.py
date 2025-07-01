# ハッシュテーブル + 頻度カウンティングパターン
# 問題2352: Equal Row and Column Pairs から抽出

def frequency_counting_pattern():
    """
    パターン: 複数の要素グループを比較し、マッチする組み合わせ数を計算

    基本アプローチ:
    1. 一方のグループをハッシュテーブルで頻度カウント
    2. もう一方のグループを順次チェック
    3. マッチした場合、頻度を結果に加算

    時間計算量: O(n*m) - n個の要素、各要素サイズm
    空間計算量: O(n*m) - ハッシュテーブルのサイズ
    """

    # Example: 2D grid の行と列のマッチング
    def equal_pairs_example(grid):
        n = len(grid)
        count = 0
        row_counter = {}

        # Step 1: 行をタプル化して頻度カウント
        for row in range(n):
            row_tuple = tuple(grid[row])
            row_counter[row_tuple] = row_counter.get(row_tuple, 0) + 1

        # Step 2: 列を順次チェックしてマッチング
        for col in range(n):
            col_tuple = tuple(grid[i][col] for i in range(n))
            if col_tuple in row_counter:
                count += row_counter[col_tuple]

        return count

    return equal_pairs_example

# 重要なポイント:
# 1. tuple vs list: ハッシュ可能性のためtupleを使用
# 2. dict.get() vs if-else: より簡潔なカウンティング
# 3. 頻度の掛け算: 同じパターンが複数回現れる場合の処理


def alternative_implementations():
    """代替実装パターン"""

    # Collections.Counter を使用
    from collections import Counter

    def using_counter(grid):
        n = len(grid)
        rows = Counter(tuple(grid[i]) for i in range(n))
        cols = Counter(tuple(grid[i][j] for i in range(n)) for j in range(n))

        return sum(rows[pattern] * cols[pattern] for pattern in rows if pattern in cols)

    # 直接比較（Counter不使用）
    def direct_comparison(grid):
        n = len(grid)
        count = 0

        for row in range(n):
            for col in range(n):
                if all(grid[row][i] == grid[i][col] for i in range(n)):
                    count += 1

        return count

    return using_counter, direct_comparison
