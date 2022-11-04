
import sys
from typing import List


def main():
    args = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(args)
    print(result)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = sys.maxsize
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price-minPrice)

        return maxProfit


if __name__ == '__main__':
    main()
