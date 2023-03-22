from typing import List


def main():
    solution = Solution()
    result = solution.shortestDistance(
        ["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
    print(result)


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        minDistance = len(wordsDict)
        firstIndex = -1
        secondIndex = -1

        for i in range(len(wordsDict)):
            target = wordsDict[i]
            if target == word1:
                firstIndex = i
            elif target == word2:
                secondIndex = i

            if firstIndex != -1 and secondIndex != -1:
                minDistance = min(minDistance, abs(firstIndex - secondIndex))

        return minDistance


if __name__ == '__main__':
    main()
