from typing import List


def main():
    args = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    result = solution.groupAnagrams(args)
    print(result)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        return groups.values()


if __name__ == '__main__':
    main()
