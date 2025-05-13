from typing import List


def main():
    args = [2, 3, 2]
    solution = Solution()
    result = solution.timeRequiredToBuy(args, 2)
    print(result)


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[i] != 0 and tickets[k] != 0:
                    tickets[i] -= 1
                    time += 1

        return time


if __name__ == '__main__':
    main()
