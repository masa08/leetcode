from typing import List


def main():
    # Test case
    words = ["a", "b", "c", "ab", "bc", "abc"]
    s = "abc"  # Expected: 3 (prefixes: "a", "ab", "abc")
    solution = Solution()
    result = solution.countPrefixes(words, s)
    print(f"Input: words={words}, s={s} -> Output: {result}")


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        result = 0
        for word in words:
            if s[:len(word)] == word:
                result += 1
        # for word in words:
        #     if s.startswith(word):
        #         result += 1
        return result


if __name__ == '__main__':
    main()
