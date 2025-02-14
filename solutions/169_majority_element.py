from typing import List


def main():
    args = [3, 2, 3]
    solution = Solution()
    result = solution.majorityElement(args)
    print(result)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pivod = len(nums)/2
        counter = {}

        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1

        for i, v in counter.items():
            if v >= pivod:
                return i


if __name__ == '__main__':
    main()
