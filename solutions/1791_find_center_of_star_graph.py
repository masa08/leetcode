from typing import List


def main():
    args = [[1, 2], [2, 3], [4, 2]]
    solution = Solution()
    result = solution.findCenter(args)
    print(result)


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        first = set(edges[0])
        second = set(edges[1])
        common = list(first & second)

        return common[0]


if __name__ == '__main__':
    main()
