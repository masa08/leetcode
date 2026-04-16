from typing import List


def main():
    solution = Solution()

    # Basic cases
    assert sorted(solution.permute([1, 2, 3])) == [
        [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert solution.permute([1]) == [[1]]

    # Edge case
    assert sorted(solution.permute([1, 2])) == [[1, 2], [2, 1]]

    print("All tests passed!")


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking: pick one unused element at a time, recurse,
        then undo the choice to try the next element.

        Time: O(n! * n) - n! permutations, each takes O(n) to copy
        Space: O(n) - recursion depth + path (excluding output)
        """
        result = []

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return result


if __name__ == '__main__':
    main()
