import heapq
from typing import List


def main():
    args = [[1, 3, 3, 2], [2, 1, 3, 4], 3]
    solution = Solution()
    result = solution.maxScore(args[0], args[1], args[2])
    print(result)


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Sort pair (nums1[i], nums2[i]) by nums2[i] in decreasing order.
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key=lambda x: -x[1])

        # Use a min-heap to maintain the top k elements.
        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)

        # The score of the first k pairs. pairs[k - 1][1] = minimum number in nums2
        answer = top_k_sum * pairs[k - 1][1]

        # Iterate over every nums2[i] as minimum from nums2.
        for i in range(k, len(nums1)):
            # Remove the smallest integer from the previous top k elements
            # then add nums1[i] to the top k elements.
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])

            # Update answer as the maximum score.
            answer = max(answer, top_k_sum * pairs[i][1])

        return answer


if __name__ == '__main__':
    main()
