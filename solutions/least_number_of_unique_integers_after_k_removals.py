from collections import Counter
import heapq
from typing import List


def main():
    arr = [4, 3, 1, 1, 3, 3, 2]
    k = 3
    solution = Solution()
    result = solution.findLeastNumOfUniqueInts(arr, k)

    print(result)


class Solution:
    # def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
    #     nums_count = sorted([b for (a,b) in Counter(arr).items()])
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
