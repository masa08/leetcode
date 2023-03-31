def main():
    args = "abcabcbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(args)
    print(result)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        left, max_length = 0, 0

        for right in range(len(s)):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            seen_chars.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == '__main__':
    main()
