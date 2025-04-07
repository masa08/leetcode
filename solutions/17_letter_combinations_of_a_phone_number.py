from typing import List


def main():
    args = "23"
    solution = Solution()
    result = solution.letterCombinations(args)
    print(result)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()

        backtrack(0, [])
        return conbinations


if __name__ == '__main__':
    main()
