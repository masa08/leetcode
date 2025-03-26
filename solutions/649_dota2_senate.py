from collections import deque


def main():
    args = "RDD"
    solution = Solution()
    result = solution.predictPartyVictory(args)
    print(result)


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # r 有権者のqueue
        # d 有権者のqueue
        # banされた人をqueueから取り除き、残っていた方の勝利
        queue_r = deque()
        queue_d = deque()
        for i, s in enumerate(senate):
            if s == 'R':
                queue_r.append(i)
            else:
                queue_d.append(i)

        while queue_r and queue_d:
            r_index = queue_r.popleft()
            d_index = queue_d.popleft()

            if r_index < d_index:
                queue_r.append(r_index + len(senate))
            else:
                queue_d.append(d_index + len(senate))

        return "Radiant" if queue_r else "Dire"

        # We can also use list instead of deque
        # but deque is faster than list
        # list pop(0) is O(n) time complexity
        # On the other hand, deque popleft() is O(1) time complexity

        # queue_r = []
        # queue_d = []
        # for i, s in enumerate(senate):
        #     if s == 'R':
        #         queue_r.append(i)
        #     else:
        #         queue_d.append(i)

        # while queue_r and queue_d:
        #     r_index = queue_r.pop(0)
        #     d_index = queue_d.pop(0)

        #     if r_index < d_index:
        #         queue_r.append(r_index + len(senate))
        #     else:
        #         queue_d.append(d_index + len(senate))

        # return "Radiant" if queue_r else "Dire"


if __name__ == '__main__':
    main()
