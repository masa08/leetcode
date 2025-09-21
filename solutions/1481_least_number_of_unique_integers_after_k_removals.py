from collections import Counter
import heapq
from typing import List


def main():
    solution = Solution()

    # テストケース1: 基本ケース
    assert solution.findLeastNumOfUniqueInts([4, 3, 1, 1, 3, 3, 2], 3) == 2

    # テストケース2: エッジケース（空配列に近い）
    assert solution.findLeastNumOfUniqueInts([1], 1) == 0

    # テストケース3: 複数の同じ頻度
    assert solution.findLeastNumOfUniqueInts([5, 5, 4], 1) == 1

    print("All tests passed!")


class Solution:
    # def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    #     nums_count = sorted(Counter(arr).values())
    #     unique_numbers = len(nums_count)
    #     index = 0

    #     while k > 0:
    #         if nums_count[index] == 1:
    #             index += 1
    #             unique_numbers-= 1
    #         else:
    #             nums_count[index] -= 1
    #         k -= 1

    #     return unique_numbers

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hp = list(Counter(arr).values())
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)

        return len(hp) + 1 if k < 0 else len(hp)


if __name__ == "__main__":
    main()
