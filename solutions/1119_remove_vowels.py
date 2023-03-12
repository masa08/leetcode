def main():
    args = "leetcodeisacommunityforcoders"
    solution = Solution()
    result = solution.removeVowels(args)
    print(result)


class Solution:
    def removeVowels(self, s: str) -> str:
        toBeDeleted = ['a', 'i', 'u', 'e', 'o']
        result = ""

        for i in range(len(s)):
            curr = s[i]
            if curr not in toBeDeleted:
                result += curr

        return result


if __name__ == '__main__':
    main()
