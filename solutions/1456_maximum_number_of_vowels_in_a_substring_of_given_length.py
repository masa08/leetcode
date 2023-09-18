def main():
    args = "abciiidef"
    solution = Solution()
    result = solution.maxVowels(args)
    print(result)


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        # calculate initial count in first range
        count = 0
        for i in range(k):
            count += int(s[i] in vowels)
        answer = count

        # sliding window
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i-k] in vowels)
            answer = max(answer, count)

        return answer


if __name__ == '__main__':
    main()
