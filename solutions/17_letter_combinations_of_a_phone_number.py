from typing import List


def main():
    solution = Solution()

    # 基本ケース
    assert solution.letterCombinations(
        "23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert solution.letterCombinations("2") == ["a", "b", "c"]

    # エッジケース
    assert solution.letterCombinations("") == []
    assert solution.letterCombinations("7") == ["p", "q", "r", "s"]

    print("All tests passed!")


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate all possible letter combinations from phone number digits

        Approach: Backtracking (Depth-First Search)
        - Choose one letter for each digit
        - Add to result when all digits are processed
        - Backtrack to try other choices

        Time Complexity: O(4^n * n) - n is number of digits, worst case 4 letters (7,9)
        Space Complexity: O(n) - recursion stack depth
        """
        if len(digits) == 0:
            return []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        conbinations = []

        def backtrack(index, path):
            if len(path) == len(digits):
                conbinations.append("".join(path))
                return

            possible_letters = letters[digits[index]]
            for pl in possible_letters:
                path.append(pl)
                backtrack(index+1, path)
                path.pop()

        backtrack(0, [])
        return conbinations


if __name__ == '__main__':
    main()
