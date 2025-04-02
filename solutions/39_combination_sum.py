from typing import List


def main():
    args1 = [2, 3, 6, 7]
    args2 = 7
    solution = Solution()
    result = solution.combinationSum(args1, args2)
    print(result)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, comb, total):
            if total == target:
                result.append(comb.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(i, comb, total + candidates[i])
                comb.pop()

        backtrack(0, [], 0)

        return result


if __name__ == '__main__':
    main()
