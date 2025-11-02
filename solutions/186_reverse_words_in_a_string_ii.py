from typing import List


def main():
    solution = Solution()

    # Basic case
    s1 = ["t", "h", "e", " ", "s", "k", "y",
          " ", "i", "s", " ", "b", "l", "u", "e"]
    solution.reverseWords(s1)
    assert s1 == ["b", "l", "u", "e", " ", "i",
                  "s", " ", "s", "k", "y", " ", "t", "h", "e"]

    # Single word
    s2 = ["h", "e", "l", "l", "o"]
    solution.reverseWords(s2)
    assert s2 == ["h", "e", "l", "l", "o"]

    # Two words
    s3 = ["a", " ", "b"]
    solution.reverseWords(s3)
    assert s3 == ["b", " ", "a"]

    print("All tests passed!")


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        Algorithm: Two-pass reversal
        1. Reverse the entire string
        2. Reverse each word individually

        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(1) - in-place modification
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
