def main():
    solution = Solution()
    result = solution.strStr("ssadbutsad", "sad")
    print(result)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # the case that haystack doesn't include the needle
        if needle not in haystack:
            return -1

        # the case that haystack includes the needle
        return haystack.find(needle)


if __name__ == '__main__':
    main()
