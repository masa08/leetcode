def main():
    solution = Solution()

    # 基本ケース
    assert solution.reverseVowels("IceCreAm") == "AceCreIm"
    assert solution.reverseVowels("leetcode") == "leotcede"

    # エッジケース
    assert solution.reverseVowels("") == ""
    assert solution.reverseVowels("a") == "a"
    assert solution.reverseVowels("bcdfg") == "bcdfg"  # 母音なし
    assert solution.reverseVowels("aeiou") == "uoiea"  # 母音のみ

    # 大文字小文字混在
    assert solution.reverseVowels("Aa") == "aA"
    assert solution.reverseVowels("HELLO") == "HOLLE"

    print("All tests passed!")


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = set(['a', 'i', 'u', 'e', 'o'])
        l, r = 0, len(s) - 1

        while l < r:
            ls = s[l].lower()
            rs = s[r].lower()

            if ls in vowels and rs in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif ls not in vowels:
                l += 1
            elif rs not in vowels:
                r -= 1

        return "".join(s)


if __name__ == '__main__':
    main()
