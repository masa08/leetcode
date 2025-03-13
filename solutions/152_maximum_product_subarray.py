from typing import List


def main():
    args = [2, 3, -2, 4]
    solution = Solution()
    result = solution.maxProduct(args)
    print(result)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # result = nums[0]

        # for i in range(len(nums)):
        #     accu = 1
        #     for j in range(i, len(nums)):
        #         accu *= nums[j]
        #         result = max(result, accu)

        # return result

        max_so_far = min_so_far = nums[0]
        result = max_so_far
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max(max_so_far*curr, min_so_far*curr))
            min_so_far = min(curr, min(max_so_far*curr, min_so_far*curr))
            max_so_far = temp_max

            result = max(max_so_far, result)

        return result


if __name__ == '__main__':
    main()
