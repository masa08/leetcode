from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Find smallest letter greater than target using binary search.

        The array is circular - if no letter is greater than target,
        return the first letter (wrap around).

        Time: O(log n), Space: O(1)
        """
        n = len(letters)

        # Binary search boundaries:
        # left_bound: largest index where letters[i] <= target
        # right_bound: smallest index where letters[i] > target
        left_bound = -1
        right_bound = n

        # Invariant: letters[left_bound] <= target < letters[right_bound]
        while right_bound - left_bound > 1:
            mid = (left_bound + right_bound) // 2

            if letters[mid] <= target:
                # mid is not the answer, search right half
                left_bound = mid
            else:
                # mid could be the answer, search left half
                right_bound = mid

        # If right_bound == n, no letter > target exists, wrap to index 0
        return letters[right_bound % n]


def main():
    solution = Solution()

    # Basic cases
    assert solution.nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert solution.nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert solution.nextGreatestLetter(["c", "f", "j"], "d") == "f"

    # Edge case: wrap around
    assert solution.nextGreatestLetter(["x", "x", "y", "y"], "z") == "x"
    assert solution.nextGreatestLetter(["c", "f", "j"], "j") == "c"

    # Duplicates
    assert solution.nextGreatestLetter(["a", "a", "b", "b"], "a") == "b"
    assert solution.nextGreatestLetter(
        ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e") == "n"

    print("All tests passed!")


if __name__ == "__main__":
    main()
