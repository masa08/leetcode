from typing import List


def main():
    solution = Solution()
    result = solution.combinationSum3(3, 9)
    print(result)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        conbinations = []

        def backtrack(remain, curr, start):
            if remain == 0 and len(curr) == k:
                conbinations.append(list(curr))
                return
            elif remain < 0 or len(curr) == k:
                return

            for i in range(start, 9):
                curr.append(i + 1)
                backtrack(remain - i - 1, curr, i + 1)
                curr.pop()

        backtrack(n, [], 0)
        return conbinations


if __name__ == '__main__':
    main()
