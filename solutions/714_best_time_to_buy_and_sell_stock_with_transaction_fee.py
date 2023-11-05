from typing import List


def main():
    args = [1, 3, 2, 8, 4, 9]
    solution = Solution()
    result = solution.maxProfit(args, 2)
    print(result)


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 取りうる行動
        # 1. 何もしない
        # 2. 株を買う
        # 3. 株を売る

        n = len(prices)
        # 株を持っている=hold or 株を持っていない=free
        hold, free = [0]*n, [0]*n
        hold[0] -= prices[0]

        for i in range(1, n):
            # 1 or 2
            hold[i] = max(hold[i-1], free[i-1] - prices[i])
            # 1 or 3
            free[i] = max(free[i-1], hold[i-1] + prices[i] - fee)

        return free[-1]


if __name__ == '__main__':
    main()
