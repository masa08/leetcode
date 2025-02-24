
import math
from typing import List


def main():
    args = [[5, 1, 3], [1, 2, 3, 4, 5], 7]
    solution = Solution()
    result = solution.successfulPairs(args[0], args[1], args[2])
    print(result)


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Bruteforce solution
        # results = []
        # for s in spells:
        #     numbers = 0
        #     for p in potions:
        #         product = s * p
        #         if product >= success:
        #             numbers += 1
        #     results.append(numbers)

        # return results

        # Binary search solution
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            min_potion_needed = math.ceil(success/spell)

            left, right = 0, m
            while left < right:
                mid = (left + right) // 2
                if potions[mid] >= min_potion_needed:
                    right = mid
                else:
                    left = mid + 1

            result.append(m - left)

        return result


if __name__ == '__main__':
    main()
