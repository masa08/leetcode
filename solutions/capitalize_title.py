def main():
    args = "capiTalIze tHe titLe"
    solution = Solution()
    result = solution.capitalizeTitle(args)
    print(result)


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        result = []

        for word in words:
            lowerWord = word.lower()
            if len(word) <= 2:
                result.append(lowerWord)
                continue
            result.append(lowerWord.capitalize())

        return " ".join(result)


if __name__ == '__main__':
    main()
