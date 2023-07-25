from typing import List


def main():
    args = [1, 2, 3, 4]
    solution = Solution()
    result = solution.productExceptSelf(args)
    print(result)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right, answer = [1] * length, [1] * length, [1] * length

        for i in range(1, length):
            left[i] = nums[i-1] * left[i-1]

        for i in reversed(range(length-1)):
            right[i] = nums[i+1] * right[i+1]

        for i in range(length):
            answer[i] = left[i] * right[i]

        return answer


if __name__ == '__main__':
    main()
