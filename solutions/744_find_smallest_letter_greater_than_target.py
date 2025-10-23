from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Binary search approach:
        - Find the first character > target
        - If no such character exists, return letters[0] (wrap around)

        Time: O(log n)
        Space: O(1)
        """
        # Edge case: target >= last letter, wrap around
        if target >= letters[-1]:
            return letters[0]

        # Binary search for smallest letter > target
        left, right = 0, len(letters) - 1

        while left < right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid

        return letters[left]


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
