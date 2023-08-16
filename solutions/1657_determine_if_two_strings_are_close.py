# https://leetcode.com/problems/determine-if-two-strings-are-close/editorial/

def main():
    solution = Solution()
    result = solution.closeStrings("abc", "bca")
    print(result)


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # check if the two words have the same length
        if len(word1) != len(word2):
            return False

        word1_map = dict()
        word2_map = dict()

        for c in word1:
            if c in word1_map:
                word1_map[c] += 1
            else:
                word1_map[c] = 1

        for c in word2:
            if c in word2_map:
                word2_map[c] += 1
            else:
                word2_map[c] = 1

        # check if the two words have the same characters (condition 1)
        if word1_map.keys() != word2_map.keys():
            return False

        # check if the two words have the same frequency of characters (condition 2)
        word1_frequency_list = list(word1_map.values())
        word2_frequency_list = list(word2_map.values())
        word1_frequency_list.sort()
        word2_frequency_list.sort()

        return word1_frequency_list == word2_frequency_list


if __name__ == '__main__':
    main()
