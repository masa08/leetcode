def main():
    solution = Solution()

    # 基本ケース
    assert solution.isSubsequence("abc", "aebdc") == True
    assert solution.isSubsequence("axc", "ahbgdc") == False

    # エッジケース
    assert solution.isSubsequence("", "ahbgdc") == True  # 空の部分列
    assert solution.isSubsequence("abc", "") == False    # 空の文字列
    assert solution.isSubsequence("", "") == True        # 両方空
    assert solution.isSubsequence("a", "a") == True      # 単文字一致
    assert solution.isSubsequence("b", "a") == False     # 単文字不一致

    print("All tests passed!")


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow = 0

        for fast in range(len(t)):
            if len(s) > slow and s[slow] == t[fast]:
                slow += 1

        return len(s) == slow


if __name__ == '__main__':
    main()
