
import sys
from typing import List


def main():
    args = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(args)
    print(result)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        benefit = 0

        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            benefit = max(benefit, prices[i] - minPrice)
        
        return benefit


if __name__ == '__main__':
    main()
