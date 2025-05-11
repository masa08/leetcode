from typing import List


def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


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
