from typing import List


def main():
    args = ["t", "h", "e", " ", "s", "k", "y",
            " ", "i", "s", " ", "b", "l", "u", "e"]
    solution = Solution()
    result = solution.reverseWords(args)
    print(result)


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(l: List[str], left: int, right: int):
            while left < right:
                l[left], l[right] = l[right], l[left]
                left, right = left+1, right-1

        def reverse_each_word(s: List[str]):
            n = len(s)
            start = end = 0

            while start < n:
                while end < n and s[end] != " ":
                    end += 1

                reverse(s, start, end-1)
                start = end + 1
                end += 1

        reverse(s, 0, len(s) - 1)
        reverse_each_word(s)


if __name__ == '__main__':
    main()
