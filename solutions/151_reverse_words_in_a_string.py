def main():
    args = "the sky is blue"
    solution = Solution()
    result = solution.reverseWords(args)
    print(result)


class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        result = []

        arr = reversed(arr)

        for element in arr:
            if element != "":
                result.append(element)
        print(result)

        return " ".join(result)


if __name__ == '__main__':
    main()
