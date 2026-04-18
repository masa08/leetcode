from typing import List


def main():
    solution = Solution()

    # Basic cases
    result1 = solution.subsets([1, 2, 3])
    assert len(result1) == 8
    assert [] in result1
    assert [1, 2, 3] in result1

    # Edge cases
    assert solution.subsets([0]) == [[], [0]]
    assert solution.subsets([]) == [[]]

    # Two elements
    result2 = solution.subsets([1, 2])
    assert sorted(result2) == [[], [1], [1, 2], [2]]

    print("All tests passed!")


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking: at each step, add current path to result,
        then try appending each remaining element (from start onward).

        Time: O(n * 2^n) - generate 2^n subsets, each takes O(n) to copy
        Space: O(n) - recursion depth
        """
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


if __name__ == "__main__":
    main()
