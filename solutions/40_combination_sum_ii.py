from typing import List


def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    solution = Solution()
    result = solution.combinationSum2(candidates, target)

    print(f"Combinations that sum to {target}: {result}")


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, comb, total):
            if total == target:
                result.append(comb.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # i > start to avoid duplicates in the same position
                # candidates[i] == candidates[i - 1] to avoid duplicates in the same combination
                # This is important to skip duplicates in the sorted list
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(i+1, comb, total + candidates[i])
                comb.pop()

        backtrack(0, [], 0)

        return result


if __name__ == '__main__':
    main()
