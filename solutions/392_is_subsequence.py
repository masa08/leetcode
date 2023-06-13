def main():
    solution = Solution()
    result = solution.isSubsequence("abc", "ahgdbc")
    print(result)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0

        for fast in range(len(t)):
            if len(s) > slow and s[slow] == t[fast]:
                slow += 1

        return len(s) == slow


if __name__ == '__main__':
    main()
