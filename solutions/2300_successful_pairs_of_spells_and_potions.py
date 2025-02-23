
from typing import List


def main():
    args = [[3, 1, 2], [1, 2, 3], 2]
    solution = Solution()
    result = solution.successfulPairs(args[0], args[1], args[2])
    print(result)


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Bruteforce solution
        results = []
        for s in spells:
            numbers = 0
            for p in potions:
                product = s * p
                if product >= success:
                    numbers += 1
            results.append(numbers)

        return results


if __name__ == '__main__':
    main()
