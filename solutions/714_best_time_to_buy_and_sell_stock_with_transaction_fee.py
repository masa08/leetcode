from typing import List


def main():
    args = [1, 3, 2, 8, 4, 9]
    solution = Solution()
    result = solution.maxProfit(args, 2)
    print(result)


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = [0]*n, [0]*n
        hold[0] -= prices[0]

        """
        Option
        1. Buy the stock.
        2. Sell the stock.
        3. Do nothing.
        """
        for i in range(1, n):
            # 3 or 1
            hold[i] = max(hold[i-1], free[i-1] - prices[i])
            # 3 or 2
            free[i] = max(free[i-1], hold[i-1] + prices[i] - fee)

        return free[-1]


if __name__ == '__main__':
    main()
