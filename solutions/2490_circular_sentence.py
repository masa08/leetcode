def main():
    args = "IuTiUtGGsNydmacGduehPPGksKQyT TmOraUbCcQdnZUCpGCYtGp p pG GCcRvZDRawqGKOiBSLwjIDOjdhnHiisfddYoeHqxOqkUvOEyI"
    solution = Solution()
    result = solution.isCircularSentence(args)
    print(result)


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        firstChar = sentence[0]
        lastChar = sentence[-1]
        if firstChar != lastChar:
            return False

        words = sentence.split(" ")
        tempLastChar = ""
        for i in range(len(words)):
            word = words[i]
            if i == 0:
                tempLastChar = word[-1]
                continue

            if word[0] != tempLastChar:
                return False
            tempLastChar = word[-1]

        return True


if __name__ == '__main__':
    main()
