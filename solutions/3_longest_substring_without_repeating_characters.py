def main():
    solution = Solution()

    # 基本ケース
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert solution.lengthOfLongestSubstring("bbbbb") == 1      # "b"
    assert solution.lengthOfLongestSubstring("pwwkew") == 3     # "wke"

    # エッジケース
    assert solution.lengthOfLongestSubstring("") == 0           # 空文字列
    assert solution.lengthOfLongestSubstring(" ") == 1          # スペース1文字
    assert solution.lengthOfLongestSubstring("abcdefg") == 7    # 全て異なる文字

    print("All tests passed!")


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, max_length = 0, 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == '__main__':
    main()
