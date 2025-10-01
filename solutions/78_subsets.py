from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking
        - Use DFS to generate all subsets
        - Each element has 2 choices: include or exclude
        - No duplicate handling needed (all elements unique)

        Time: O(n * 2^n) - generate 2^n subsets, each takes O(n) to copy
        Space: O(n) - recursion depth
        """
        # Edge case
        if not nums:
            return [[]]

        result = []

        def backtrack(start: int, path: List[int]):
            # Add current subset
            result.append(path[:])

            # Try adding each remaining element
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


def main():
    solution = Solution()

    # Basic cases
    result1 = solution.subsets([1, 2, 3])
    assert len(result1) == 8  # 2^3
    assert [] in result1
    assert [1, 2, 3] in result1

    # Edge cases
    assert solution.subsets([0]) == [[], [0]]
    assert solution.subsets([1]) == [[], [1]]

    # Two elements
    result2 = solution.subsets([1, 2])
    assert len(result2) == 4  # 2^2
    assert sorted([sorted(s) for s in result2]) == [[], [1], [1, 2], [2]]

    print("All tests passed!")


if __name__ == "__main__":
    main()
