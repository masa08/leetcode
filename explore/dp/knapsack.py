def main():
    weights = [2, 5, 4]
    values = [6, 9, 5]
    capacity = 6

    solution = Solution()
    print(solution.knapsack(weights, values, capacity))


class Solution:
    def knapsack(self, weights, values, capacity):
        items_count = len(weights)
        # item_count数 * capacity数の2次元配列を作成
        dp = [[0 for _ in range(capacity + 1)] for _ in range(items_count + 1)]

        for item in range(1, items_count + 1):
            item_weight = weights[item - 1]
            item_value = values[item - 1]

            # 対象itemを入れる場合と入れない場合で、より価値の高い方を選択し、dpに格納
            for curr_weight in range(1, capacity + 1):
                if curr_weight >= item_weight:
                    dp[item][curr_weight] = max(
                        item_value + dp[item - 1][curr_weight - item_weight],
                        dp[item-1][curr_weight]
                    )
                else:
                    dp[item][curr_weight] = dp[item - 1][curr_weight]

        return dp[-1][-1]


if __name__ == '__main__':
    main()
