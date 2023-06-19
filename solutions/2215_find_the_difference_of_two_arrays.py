from typing import List


def main():
    args = [1, 2, 3]
    args2 = [2, 4, 6]
    solution = Solution()
    result = solution.findDifference(args, args2)
    print(result)


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = []

        set1 = set(nums1)
        set2 = set(nums2)
        result.append(set1-set2)
        result.append(set2-set1)

        return result


if __name__ == '__main__':
    main()
