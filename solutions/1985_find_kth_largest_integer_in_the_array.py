import heapq
from typing import List


def main():
    args = ["3", "6", "7", "10"]
    k = 4
    solution = Solution()
    result = solution.kthLargestNumber(args, k)
    print(result)


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) * -1 for num in nums]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)

        result = heapq.heappop(nums) * -1

        return str(result)


if __name__ == '__main__':
    main()
