from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Backtracking with duplicate handling
        - Sort first to group duplicates together
        - Skip duplicates at the same recursion level
        - Use DFS to generate all unique subsets

        Time: O(n * 2^n) - same as subsets without duplicates
        Space: O(n) - recursion depth
        """
        if not nums:
            return [[]]

        result = []
        sorted_nums = sorted(nums)

        def backtrack(start_index, current_subset):
            result.append(current_subset[:])

            for i in range(start_index, len(sorted_nums)):
                is_not_first_element = i > start_index
                is_same_as_previous = sorted_nums[i] == sorted_nums[i-1]
                # Skip duplicate at same level to avoid generating same subset twice
                # Works because array is sorted (duplicates are adjacent)
                is_duplicate_at_same_level = is_not_first_element and is_same_as_previous

                if is_duplicate_at_same_level:
                    continue

                current_subset.append(sorted_nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        backtrack(0, [])
        return result


def main():
    solution = Solution()

    # Basic cases
    assert sorted(solution.subsetsWithDup([1, 2, 2])) == sorted(
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    assert sorted(solution.subsetsWithDup([0])) == sorted([[], [0]])

    # Edge cases
    assert solution.subsetsWithDup([1]) == [[], [1]]
    assert sorted(solution.subsetsWithDup([1, 1])) == sorted([[], [1], [1, 1]])

    # Multiple duplicates
    # [], [1], [1,1], [1,1,1]
    assert len(solution.subsetsWithDup([1, 1, 1])) == 4

    print("All tests passed!")


if __name__ == "__main__":
    main()
