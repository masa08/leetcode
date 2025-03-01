import math
from typing import List


def main():
    args = [[3, 6, 7, 11], 8]
    solution = Solution()
    result = solution.minEatingSpeed(args[0], args[1])
    print(result)


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left+right) // 2
            hours = sum(math.ceil(pile/mid) for pile in piles)

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    main()
