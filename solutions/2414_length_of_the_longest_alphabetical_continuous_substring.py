def main():
    args = "abcde"
    solution = Solution()
    result = solution.longestContinuousSubstring(args)
    print(result)


class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        length, max_length = 1, 1

        for i in range(len(s)-1):
            if ord(s[i])+1 == ord(s[i+1]):
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1

        return max(length, max_length)


if __name__ == '__main__':
    main()
