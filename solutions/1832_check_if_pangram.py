def main():
    args = "thequickbrownfoxjumpsoverthelazydog"
    solution = Solution()
    result = solution.checkIfPangram(args)
    print(result)


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # allAlphabet = [chr(ord("a")+i) for i in range(26)]
        # seen = []

        # for s in sentence:
        #     if s in seen:
        #         continue
        #     else:
        #         seen.append(s)

        # return allAlphabet == sorted(seen)

        allAlphabet = [chr(ord("a")+i) for i in range(26)]

        for a in allAlphabet:
            if a not in sentence:
                return False

        return True


if __name__ == '__main__':
    main()
