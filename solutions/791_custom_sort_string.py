from collections import defaultdict


def main():
    solution = Solution()

    # テストケース
    assert solution.customSortString("cba", "abcd") == "cdba"
    assert solution.customSortString("bcafg", "abcd") == "bdca"
    print("All tests passed!")


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic_order = defaultdict(int)

        for i in range(len(order)):
            dic_order[order[i]] = i

        return "".join(sorted(s, key=lambda c: dic_order[c]))


if __name__ == '__main__':
    main()
