from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert sorted(solution.combinationSum([2, 3, 6, 7], 7)) == [[2, 2, 3], [7]]
    assert sorted(solution.combinationSum([2, 3, 5], 8)) == [
        [2, 2, 2, 2], [2, 3, 3], [3, 5]]

    # Edge cases
    assert solution.combinationSum([2], 1) == []      # No solution
    assert solution.combinationSum(
        [1], 2) == [[1, 1]]  # Single element repeated
    assert solution.combinationSum([7], 7) == [[7]]    # Exact match

    print("All tests passed!")


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking: try each candidate from start onward, allowing reuse
        of the same element (pass i instead of i+1 to recurse).

        Time: O(n^(target/min)) - branching factor n, depth up to target/min(candidates)
        Space: O(target/min) - recursion depth
        """
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result


if __name__ == '__main__':
    main()
