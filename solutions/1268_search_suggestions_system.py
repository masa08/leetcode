from bisect import bisect_left
from typing import List


def main():
    args = [["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"]
    solution = Solution()
    result = solution.suggestedProducts(*args)
    print(result)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        result = []
        prefix = ""

        for char in searchWord:
            prefix += char
            index = bisect_left(products, prefix)
            suggestions = []

            for i in range(index, min(index + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])

            result.append(suggestions)

        return result


if __name__ == '__main__':
    main()
