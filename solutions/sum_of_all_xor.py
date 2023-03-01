from typing import List


def main():
    args = [5, 1, 6]
    solution = Solution()
    result = solution.subsetXORSum(args)
    print(result)


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        subsets = [0]

        for n in nums:
            # eg: [5,1,6]
            # 1: [0]
            # 2: [0,5]
            # 3: [0,5,1,4]
            new_subsets = subsets.copy()
            for s in subsets:
                xorResult = s ^ n
                new_subsets.append(xorResult)
                result += xorResult
            subsets = new_subsets

        return result


if __name__ == '__main__':
    main()
