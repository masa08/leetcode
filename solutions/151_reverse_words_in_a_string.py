def main():
    args = "  the  sky is blue   "
    solution = Solution()
    result = solution.reverseWords(args)
    print(result)


class Solution:
    def __trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1

        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        output = []
        while left <= right:
            if s[left] == ' ' and output and output[-1] == ' ':
                left += 1
                continue

            output.append(s[left])
            left += 1

        return output

    def __reverse_list(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def __reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = 0

        while start < n:
            end = start
            while end < n and l[end] != ' ':
                end += 1
            self.__reverse_list(l, start, end - 1)
            start = end + 1

    def reverseWords(self, s: str) -> str:
        trimmed_list = self.__trim_spaces(s)
        self.__reverse_list(trimmed_list, 0, len(trimmed_list) - 1)
        self.__reverse_each_word(trimmed_list)

        return ''.join(trimmed_list)


if __name__ == '__main__':
    main()
