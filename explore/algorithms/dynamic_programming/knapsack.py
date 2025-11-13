"""
ナップサック問題 (Knapsack Problem)

容量制限のあるナップサックに、価値と重さを持つアイテムを詰めて、
価値の合計を最大化する問題。

主な種類:
1. 0/1ナップサック: 各アイテムを0回または1回使用
2. 無制限ナップサック: 各アイテムを何度でも使用可能
"""

from typing import List


def print_dp_array(dp: List, label: str = ""):
    """DPテーブルを見やすく表示"""
    if label:
        print(f"{label}")
    print(f"  容量: {' '.join(f'{i:3}' for i in range(len(dp)))}")
    print(f"  価値: {' '.join(f'{v:3}' for v in dp)}")


def print_separator(char="=", length=60):
    """セパレーター表示"""
    print(char * length)


class Knapsack01:
    """
    0/1 ナップサック問題

    各アイテムを「入れる」か「入れない」かの2択。

    状態定義: dp[i][w] = 最初のi個のアイテムを使い、重さ制限wでの最大価値
    遷移式:
        dp[i][w] = max(
            dp[i-1][w],                          # i番目を入れない
            dp[i-1][w-weight[i]] + value[i]      # i番目を入れる
        )
    """

    def solve_2d(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        2次元DP解法 - 理解重視版
        Time: O(n * capacity)
        Space: O(n * capacity)

        【具体例で理解】weights=[2,3], values=[3,4], capacity=5

        DPテーブル dp[i][w] の意味:
        - i: 最初のi個のアイテムを「検討対象」とする
        - w: ナップサックの残り容量
        - 値: その条件での「最大価値」

        初期状態: dp[0][w] = 0 (アイテム0個 → 価値0)

        【ステップバイステップ】
        i=1: アイテム0 (weight=2, value=3) を検討
          w=0,1: 容量不足 → dp[1][w]=0
          w=2~5: 入れる → dp[1][w]=3

        i=2: アイテム1 (weight=3, value=4) を検討
          w=0~2: アイテム1は入らない → 前の状態を継承
          w=3,4: アイテム1のみ入れる → dp[2][w]=4
          w=5: 両方入る (2+3=5) → dp[2][5]=max(4, 3+4)=7

        【重要な思考ポイント】
        各 dp[i][w] で2つの選択肢を比較:
        1. 入れない: dp[i-1][w] (前回の最適解をそのまま継承)
        2. 入れる: dp[i-1][w-weight] + value (容量を使って価値を得る)
        """
        n = len(weights)

        # DPテーブル初期化: dp[i][w] = 最初のi個で容量w時の最大価値
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        # アイテムを1つずつ検討
        for i in range(1, n + 1):
            weight = weights[i - 1]  # 現在のアイテムの重さ
            value = values[i - 1]    # 現在のアイテムの価値

            # すべての容量パターンを試す
            for w in range(capacity + 1):
                # 選択肢1: i番目のアイテムを入れない
                # → 前回(i-1個目まで)の最適解をそのまま使う
                dp[i][w] = dp[i - 1][w]

                # 選択肢2: i番目のアイテムを入れる（容量が足りる場合のみ）
                if w >= weight:
                    # 「容量w-weightの状態」にアイテムiを追加した価値
                    include_value = dp[i - 1][w - weight] + value

                    # 入れない場合 vs 入れる場合 の良い方を選択
                    dp[i][w] = max(dp[i][w], include_value)

                # デバッグ時はここでprint(f"dp[{i}][{w}] = {dp[i][w]}")

        # dp[n][capacity] = 全アイテム検討後、満容量での最大価値
        return dp[n][capacity]

    def solve_1d(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        1次元DP解法（空間最適化） - 理解重視版
        Time: O(n * capacity)
        Space: O(capacity)

        【なぜ後ろから更新するのか？】
        weights=[2,3], values=[3,4], capacity=5 で考える

        dp配列: [w=0, w=1, w=2, w=3, w=4, w=5]

        ■ アイテム0 (weight=2, value=3) 処理前:
        dp = [0, 0, 0, 0, 0, 0]

        【前から更新すると起きる問題】
        w=2: dp[2] = max(0, dp[0]+3) = 3  ✓
        w=4: dp[4] = max(0, dp[2]+3) = 6  ✗ 同じアイテムを2回使ってしまう！
             ↑ dp[2]がすでに更新済み

        【後ろから更新する理由】
        w=5: dp[5] = max(0, dp[3]+3) = 3  ✓
        w=4: dp[4] = max(0, dp[2]+3) = 3  ✓
        w=3: dp[3] = max(0, dp[1]+3) = 3  ✓
        w=2: dp[2] = max(0, dp[0]+3) = 3  ✓
             ↑ dp[2~5]はまだ更新されていない（前回の状態を保持）

        結果: dp = [0, 0, 3, 3, 3, 3]

        ■ アイテム1 (weight=3, value=4) を処理:
        w=5: dp[5] = max(3, dp[2]+4) = max(3, 7) = 7  ✓ 両方入る！
        w=4: dp[4] = max(3, dp[1]+4) = max(3, 4) = 4
        w=3: dp[3] = max(3, dp[0]+4) = max(3, 4) = 4

        最終: dp = [0, 0, 3, 4, 4, 7]

        【核心原理】
        後ろから更新 → dp[w-weight]は「前回のループでの値」= dp[i-1][w-weight]
        前から更新 → dp[w-weight]は「今回すでに更新済みの値」= dp[i][w-weight]

        0/1ナップサックは各アイテムを1回だけ使うので、
        「前回の状態」を参照する必要がある → 後ろから更新
        """
        dp = [0] * (capacity + 1)

        # 各アイテムを検討
        for i in range(len(weights)):
            weight = weights[i]
            value = values[i]

            # 【重要】後ろから更新: 同じアイテムを複数回使わないため
            # range(capacity, weight-1, -1) = [capacity, capacity-1, ..., weight]
            for w in range(capacity, weight - 1, -1):
                # dp[w-weight]は「まだ今回更新されていない」= 前回の状態
                dp[w] = max(
                    dp[w],              # アイテムiを入れない
                    dp[w - weight] + value  # アイテムiを入れる
                )

        return dp[capacity]

    def solve_1d_verbose(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        1次元DP解法（詳細トレース版）
        実行過程を視覚化して理解を深める
        """
        dp = [0] * (capacity + 1)

        print("\n【0/1ナップサック - 実行トレース】")
        print_dp_array(dp, "初期状態:")
        print()

        for i in range(len(weights)):
            weight = weights[i]
            value = values[i]

            print(f"アイテム{i} (重さ={weight}, 価値={value}) を処理中...")
            print(f"  更新方向: 後ろから (capacity={capacity} → {weight})")

            # 後ろから更新
            for w in range(capacity, weight - 1, -1):
                old_value = dp[w]
                new_value = dp[w - weight] + value

                if new_value > old_value:
                    dp[w] = new_value
                    print(
                        f"    w={w}: {old_value} → {new_value} (入れる: dp[{w-weight}]+{value})")

            print_dp_array(dp, f"  処理後:")
            print()

        print(f"最終結果: 容量{capacity}での最大価値 = {dp[capacity]}")
        return dp[capacity]

    def solve_memo(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        メモ化再帰解法
        Time: O(n * capacity)
        Space: O(n * capacity)
        """
        n = len(weights)
        memo = {}

        def dp(i: int, w: int) -> int:
            """i番目以降のアイテムで、残り容量wの最大価値"""
            # 基本ケース
            if i == n or w == 0:
                return 0

            # メモチェック
            if (i, w) in memo:
                return memo[(i, w)]

            # i番目を入れない場合
            result = dp(i + 1, w)

            # i番目を入れる場合（容量が足りれば）
            if w >= weights[i]:
                result = max(result, dp(i + 1, w - weights[i]) + values[i])

            memo[(i, w)] = result
            return result

        return dp(0, capacity)

    def solve_with_items(self, weights: List[int], values: List[int], capacity: int) -> tuple:
        """
        選択したアイテムも返す
        Returns: (最大価値, 選択したアイテムのインデックスリスト)
        """
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        # DP テーブル構築
        for i in range(1, n + 1):
            weight = weights[i - 1]
            value = values[i - 1]

            for w in range(capacity + 1):
                dp[i][w] = dp[i - 1][w]
                if w >= weight:
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

        # バックトラック: 選択したアイテムを復元
        selected = []
        w = capacity
        for i in range(n, 0, -1):
            # i番目のアイテムが選択されたか判定
            if dp[i][w] != dp[i - 1][w]:
                selected.append(i - 1)  # 0-indexed
                w -= weights[i - 1]

        selected.reverse()
        return dp[n][capacity], selected


class UnboundedKnapsack:
    """
    無制限ナップサック問題

    各アイテムを何度でも使用可能。

    状態定義: dp[w] = 重さ制限wでの最大価値
    遷移式:
        dp[w] = max(dp[w], dp[w-weight[i]] + value[i])  for all i
    """

    def solve(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        1次元DP解法
        Time: O(n * capacity)
        Space: O(capacity)

        ポイント: 前から更新することで、同じアイテムを複数回使える
        """
        dp = [0] * (capacity + 1)

        for w in range(capacity + 1):
            for i in range(len(weights)):
                if w >= weights[i]:
                    dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

        return dp[capacity]

    def solve_alternative(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        別の実装方法（アイテムごとにループ） - 理解重視版
        Time: O(n * capacity)
        Space: O(capacity)

        【0/1との違い: 前から更新する理由】
        weights=[3], values=[50], capacity=8 で考える

        ■ アイテム0 (weight=3, value=50) を処理:
        dp = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        【前から更新（無制限ナップサック）】
        w=3: dp[3] = max(0, dp[0]+50) = 50  (1個目)
        w=6: dp[6] = max(0, dp[3]+50) = 100  (2個目) ✓ 同じアイテムを再利用！
             ↑ dp[3]は今回のループですでに更新済み = 50

        w=9: dp[9] = max(0, dp[6]+50) = 150  (3個目) ✓

        結果: dp = [0, 0, 0, 50, 50, 50, 100, 100, 100]

        【核心原理】
        前から更新 → dp[w-weight]は「今回すでに更新済み」= 同じアイテムを使った状態
        後ろから更新 → dp[w-weight]は「まだ未更新」= 前回の状態

        無制限ナップサックは同じアイテムを何度でも使えるので、
        「すでに更新済みの状態」を参照したい → 前から更新

        【0/1との比較】
        0/1: range(capacity, weight-1, -1) → 後ろから (各1回)
        無制限: range(weight, capacity+1) → 前から (何度でも)
        """
        dp = [0] * (capacity + 1)

        for i in range(len(weights)):
            weight = weights[i]
            value = values[i]

            # 【重要】前から更新: 同じアイテムを複数回使うため
            # range(weight, capacity+1) = [weight, weight+1, ..., capacity]
            for w in range(weight, capacity + 1):
                # dp[w-weight]は「今回すでに更新済み」= 同じアイテムを使った状態
                dp[w] = max(
                    dp[w],              # アイテムiを追加しない
                    dp[w - weight] + value  # アイテムiをもう1個追加
                )

        return dp[capacity]

    def solve_verbose(self, weights: List[int], values: List[int], capacity: int) -> int:
        """
        無制限ナップサック（詳細トレース版）
        0/1との違いを視覚化
        """
        dp = [0] * (capacity + 1)

        print("\n【無制限ナップサック - 実行トレース】")
        print_dp_array(dp, "初期状態:")
        print()

        for i in range(len(weights)):
            weight = weights[i]
            value = values[i]

            print(f"アイテム{i} (重さ={weight}, 価値={value}) を処理中...")
            print(f"  更新方向: 前から (weight={weight} → capacity={capacity})")
            print(f"  ※同じアイテムを複数回使えます")

            # 前から更新
            for w in range(weight, capacity + 1):
                old_value = dp[w]
                new_value = dp[w - weight] + value

                if new_value > old_value:
                    dp[w] = new_value
                    # すでに更新されたdp[w-weight]を使うことで、同じアイテムを複数回使える
                    used_count = new_value // value if value > 0 else 0
                    print(
                        f"    w={w}: {old_value} → {new_value} (dp[{w-weight}]+{value})")

            print_dp_array(dp, f"  処理後:")
            print()

        print(f"最終結果: 容量{capacity}での最大価値 = {dp[capacity]}")
        return dp[capacity]


class KnapsackVariations:
    """ナップサック問題の変種"""

    def coin_change_min_coins(self, coins: List[int], amount: int) -> int:
        """
        Coin Change: 最小コイン数
        LeetCode 322

        無制限ナップサックの応用。価値=1、重さ=コインの額面
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] = min(dp[a], dp[a - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    def coin_change_ways(self, coins: List[int], amount: int) -> int:
        """
        Coin Change II: 組み合わせの数
        LeetCode 518

        無制限ナップサックで組み合わせ数を求める
        """
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]

    def can_partition(self, nums: List[int]) -> bool:
        """
        Partition Equal Subset Sum
        LeetCode 416

        0/1ナップサックの応用。配列を2つの等しい部分集合に分割可能か
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # 後ろから更新（0/1ナップサック）
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]

        return dp[target]

    def find_target_sum_ways(self, nums: List[int], target: int) -> int:
        """
        Target Sum
        LeetCode 494

        +/-を割り当てて目標値にする方法の数
        """
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        # 問題を部分集合和に変換
        # P: 正の数の集合, N: 負の数の集合
        # P - N = target, P + N = total
        # => P = (target + total) / 2
        subset_sum = (target + total) // 2

        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]


def main():
    """テストケース - 理解重視版"""

    print_separator("=", 70)
    print("ナップサック問題 - 詳細実行トレース")
    print_separator("=", 70)

    # ========================================
    # Part 1: 0/1ナップサック - 詳細トレース
    # ========================================
    print_separator()
    print("Part 1: 0/1ナップサック（各アイテムは1回だけ使用可能）")
    print_separator()

    # 小さい例で詳細トレース
    weights_simple = [2, 3]
    values_simple = [3, 4]
    capacity_simple = 5

    knapsack_01 = Knapsack01()

    print(f"\n【問題設定】")
    print(f"  アイテム0: 重さ={weights_simple[0]}, 価値={values_simple[0]}")
    print(f"  アイテム1: 重さ={weights_simple[1]}, 価値={values_simple[1]}")
    print(f"  ナップサック容量: {capacity_simple}")

    result_verbose = knapsack_01.solve_1d_verbose(
        weights_simple, values_simple, capacity_simple)

    # ========================================
    # Part 2: 無制限ナップサック - 詳細トレース
    # ========================================
    print_separator()
    print("Part 2: 無制限ナップサック（各アイテムは何度でも使用可能）")
    print_separator()

    # 同じアイテムを複数回使う例
    weights_unbounded = [3]
    values_unbounded = [50]
    capacity_unbounded = 9

    unbounded = UnboundedKnapsack()

    print(f"\n【問題設定】")
    print(f"  アイテム0: 重さ={weights_unbounded[0]}, 価値={values_unbounded[0]}")
    print(f"  ナップサック容量: {capacity_unbounded}")
    print(f"  期待: アイテム0を3回使う → 価値 = 50×3 = 150")

    result_unbounded_verbose = unbounded.solve_verbose(
        weights_unbounded, values_unbounded, capacity_unbounded)

    # ========================================
    # Part 3: 0/1 vs 無制限の比較
    # ========================================
    print_separator()
    print("Part 3: 0/1 vs 無制限 - 直接比較")
    print_separator()

    weights_compare = [3]
    values_compare = [50]
    capacity_compare = 9

    print(f"\n【同じ入力で比較】")
    print(f"  アイテム: 重さ={weights_compare[0]}, 価値={values_compare[0]}")
    print(f"  容量: {capacity_compare}")

    result_01 = knapsack_01.solve_1d(
        weights_compare, values_compare, capacity_compare)
    result_unbounded = unbounded.solve_alternative(
        weights_compare, values_compare, capacity_compare)

    print(f"\n  0/1ナップサック結果: {result_01} (アイテムは1回のみ)")
    print(
        f"  無制限ナップサック結果: {result_unbounded} (アイテムを{result_unbounded//values_compare[0]}回使用)")

    # ========================================
    # Part 4: 通常テスト（結果検証）
    # ========================================
    print_separator()
    print("Part 4: 通常テスト - すべての手法で結果を検証")
    print_separator()

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8

    print(f"\n【0/1ナップサック】")
    print(f"  入力: weights={weights}, values={values}, capacity={capacity}")

    result_2d = knapsack_01.solve_2d(weights, values, capacity)
    result_1d = knapsack_01.solve_1d(weights, values, capacity)
    result_memo = knapsack_01.solve_memo(weights, values, capacity)
    max_value, selected = knapsack_01.solve_with_items(
        weights, values, capacity)

    print(f"  2次元DP: {result_2d}")
    print(f"  1次元DP: {result_1d}")
    print(f"  メモ化再帰: {result_memo}")
    print(f"  選択アイテム: {selected} (価値={max_value})")

    selected_items_detail = [(i, weights[i], values[i]) for i in selected]
    print(f"  詳細: {selected_items_detail}")

    assert result_2d == result_1d == result_memo == max_value == 10

    # 無制限ナップサック
    print(f"\n【無制限ナップサック】")
    weights2 = [1, 3, 4]
    values2 = [15, 50, 60]
    capacity2 = 8

    result = unbounded.solve(weights2, values2, capacity2)
    print(f"  入力: weights={weights2}, values={values2}, capacity={capacity2}")
    print(f"  最大価値: {result}")
    print(f"  最適解: アイテム1(重さ3,価値50)×2回 + アイテム0(重さ1,価値15)×2回 = 130")
    assert result == 130

    # 変種問題
    print(f"\n【ナップサック変種】")
    variations = KnapsackVariations()

    # Coin Change
    coins = [1, 2, 5]
    amount = 11
    min_coins = variations.coin_change_min_coins(coins, amount)
    print(
        f"  Coin Change: coins={coins}, amount={amount} -> {min_coins}枚 (5+5+1)")
    assert min_coins == 3

    # Coin Change II
    ways = variations.coin_change_ways(coins, amount)
    print(f"  Coin Change II: 組み合わせ数 = {ways}通り")

    # Partition Equal Subset Sum
    nums = [1, 5, 11, 5]
    can_partition = variations.can_partition(nums)
    print(f"  Partition: {nums} -> {can_partition} ([1,5,5] と [11])")
    assert can_partition == True

    # Target Sum
    nums2 = [1, 1, 1, 1, 1]
    target = 3
    ways2 = variations.find_target_sum_ways(nums2, target)
    print(f"  Target Sum: {nums2}, target={target} -> {ways2}通り")
    assert ways2 == 5

    # まとめ
    print_separator("=", 70)
    print("✅ すべてのテスト完了！")
    print_separator("=", 70)
    print("\n【学習ポイントまとめ】")
    print("1. 0/1ナップサック: 後ろから更新 → 各アイテム1回のみ")
    print("2. 無制限ナップサック: 前から更新 → 同じアイテムを複数回使用可能")
    print("3. 更新方向が「同じアイテムの再利用」を制御する鍵")
    print("4. DPテーブルの変化を追うことで、アルゴリズムの動作を理解")
    print_separator("=", 70)


if __name__ == '__main__':
    main()
