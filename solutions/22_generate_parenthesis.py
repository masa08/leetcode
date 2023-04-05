from typing import List


def main():
    args = 2
    solution = Solution()
    result = solution.generateParenthesis(args)
    print(result)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(s, left, right):
            if left == 0 and right == 0:
                result.append(s)
                return

            if left > 0:
                backtrack(s+'(', left-1, right)

            if right > 0 and left < right:
                backtrack(s+')', left, right-1)

        backtrack('', n, n)
        return result


if __name__ == '__main__':
    main()
