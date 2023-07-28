from typing import List


def main():
    args = [1, 2, 2, 1, 1, 3]
    solution = Solution()
    result = solution.uniqueOccurrences(args)
    print(result)


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = dict()
        for i in range(len(arr)):
            if arr[i] in dic:
                dic[arr[i]] += 1
            else:
                dic[arr[i]] = 1

        number = set()
        for v in dic.values():
            number.add(v)

        return len(number) == len(dic)


if __name__ == '__main__':
    main()
