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

        # Convert input lists to sets to find distinct elements
        set1 = set(nums1)
        set2 = set(nums2)

        # Find elements in set1 that are not in set2 and add to result
        result.append(set1-set2)
        # Find elements in set2 that are not in set1 and add to result
        result.append(set2-set1)

        return result


if __name__ == '__main__':
    main()
