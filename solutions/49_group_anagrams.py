from collections import defaultdict
from typing import List


def main():
    solution = Solution()

    # Test case 1
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))

    # Test case 2
    strs = [""]
    print(solution.groupAnagrams(strs))

    # Test case 3
    strs = ["a"]
    print(solution.groupAnagrams(strs))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for st in strs:
            counter = [0] * 26
            for c in st:
                counter[ord(c)-ord('a')] += 1
            groups[tuple(counter)].append(st)

        return list(groups.values())


if __name__ == '__main__':
    main()
