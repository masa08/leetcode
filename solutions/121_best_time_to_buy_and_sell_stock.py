from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([1, 2]) == 1

    # エッジケース
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0  # 価格が下がり続ける → 利益なし
    assert solution.maxProfit([1]) == 0  # 1要素 → 売買できない

    print("All tests passed!")


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        「今日までの最安値で買っていたら、今日売ったときいくら儲かるか？」
        を毎日チェックして、最大の利益を記録する。

        例: [7, 1, 5, 3, 6, 4]
          Day 1: 価格7 → 最安値7, 利益 7-7=0
          Day 2: 価格1 → 最安値1, 利益 1-1=0
          Day 3: 価格5 → 最安値1, 利益 5-1=4 ★
          Day 4: 価格3 → 最安値1, 利益 3-1=2
          Day 5: 価格6 → 最安値1, 利益 6-1=5 ★★ 最大!
          Day 6: 価格4 → 最安値1, 利益 4-1=3

        Time: O(n) - 1回のループで完了
        Space: O(1) - 変数2つだけ
        """
        min_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)

        return profit


if __name__ == '__main__':
    main()
