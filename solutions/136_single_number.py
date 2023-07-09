from typing import List


def main():
    args = [2, 2, 1]
    solution = Solution()
    result = solution.singleNumber(args)
    print(result)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}

        for n in nums:
            if n in mapping:
                mapping[n] += 1
            else:
                mapping[n] = 1

        for k in mapping:
            v = mapping[k]
            if v == 1:
                return k


if __name__ == '__main__':
    main()
