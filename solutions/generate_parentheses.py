from typing import List


def main():
    args = 3
    solution = Solution()
    result = solution.generateParenthesis(args)
    print(result)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(ans, s, left, right):
            if left == 0 and right == 0:
                ans.append(s)

            if left > 0:
                helper(ans, s+'(', left-1, right)

            if right > 0 and left < right:
                helper(ans, s+')', left, right-1)

        ans = []
        helper(ans, '', n, n)

        return ans


if __name__ == '__main__':
    main()
