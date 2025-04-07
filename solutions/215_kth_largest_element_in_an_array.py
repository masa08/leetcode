import heapq
from typing import List


def main():
    args = [3, 2, 1, 5, 6, 4]
    solution = Solution()
    result = solution.findKthLargest(args, 2)
    print(result)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sort
        # sorted_num = sorted(nums, reverse=True)
        # return sorted_num[k-1]

        # heap1
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap, num)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return heap[0]

        # heap2
        nums = [-1 * num for num in nums]
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)

        return heapq.heappop(nums) * -1


if __name__ == '__main__':
    main()
