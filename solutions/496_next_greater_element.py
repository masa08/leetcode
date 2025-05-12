from typing import List


def main():
    args = [4, 1, 2]
    args2 = [1, 3, 4, 2]
    solution = Solution()
    result = solution.nextGreaterElement(args, args2)
    print(result)


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            target = nums1[i]
            index = nums2.index(target)
            for j in range(index, len(nums2)):
                if nums2[j] > target:
                    result.append(nums2[j])
                    break
            if len(result) < i+1:
                result.append(-1)
        return result


if __name__ == '__main__':
    main()
