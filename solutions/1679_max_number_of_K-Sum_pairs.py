from typing import List


def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # two pointer way
        # count = 0
        # nums = sorted(nums)
        # left, right = 0, len(nums)-1

        # while left < right:
        #     if nums[left] + nums[right] == k:
        #         count += 1
        #         left += 1
        #         right -= 1
        #     elif nums[left] + nums[right] < k:
        #         left += 1
        #     else:
        #         right -= 1

        # return count

        # hash map way
        mapping = {}
        count = 0

        for n in nums:
            if n in mapping:
                mapping[n] += 1
            else:
                mapping[n] = 1

        for i in range(len(nums)):
            current = nums[i]
            complement = k - nums[i]
            isCount = (current in mapping and mapping[current] > 0) and (
                complement in mapping and mapping[complement] > 0)
            if isCount:
                if current == complement and mapping[current] < 2:
                    continue
                mapping[current] -= 1
                mapping[complement] -= 1
                count += 1

        return count


if __name__ == '__main__':
    main()
