from typing import List


def main():
    args = [8, 4, 6, 2, 3]
    solution = Solution()
    result = solution.finalPrices(args)
    print(result)


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []

        for i in range(len(prices)):
            item = prices[i]

            for j in range(i+1, len(prices)):
                if item >= prices[j]:
                    result.append(item-prices[j])
                    break

            if len(result) != i+1:
                result.append(item)

        return result


if __name__ == '__main__':
    main()
