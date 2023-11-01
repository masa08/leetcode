from typing import List


def main():
    args = "leetcode"
    solution = Solution()
    result = solution.wordBreak(args, ["leet", "code"])
    print(result)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for word in wordDict:
                if i < len(word)-1:
                    continue

                if i == len(word)-1 or dp[i-len(word)]:
                    if s[i-len(word)+1:i+1] == word:
                        dp[i] = True
                        break
        return dp[-1]


if __name__ == '__main__':
    main()
