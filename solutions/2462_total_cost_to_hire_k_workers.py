from heapq import heapify, heappop, heappush
from typing import List


def main():
    args = [[17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4]
    solution = Solution()
    result = solution.totalCost(args[0], args[1], args[2])
    print(result)


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head_workers = costs[:candidates]
        tail_workers = costs[max(candidates, len(costs) - candidates):]
        heapify(head_workers)
        heapify(tail_workers)

        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            if not tail_workers or head_workers and head_workers[0] <= tail_workers[0]:
                answer += heappop(head_workers)

                if next_head <= next_tail:
                    heappush(head_workers, costs[next_head])
                    next_head += 1
            else:
                answer += heappop(tail_workers)

                if next_head <= next_tail:
                    heappush(tail_workers, costs[next_tail])
                    next_tail -= 1

        return answer


if __name__ == '__main__':
    main()
