def main():
    args = "abcabcbb"
    solution = Solution()
    result = solution.lengthOfLongestSubstring(args)
    print(result)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left, res = 0, 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            res = max(res, right-left+1)
        return res


if __name__ == '__main__':
    main()
