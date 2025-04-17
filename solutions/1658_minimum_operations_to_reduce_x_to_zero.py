from typing import List


def main():
    args = [1, 1, 4, 2, 3]
    x = 5
    solution = Solution()
    result = solution.minOperations(args, x)
    print(result)


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        maxi = -1
        left = 0
        current = 0

        for right in range(n):
            # sum([left ,..., right]) = total - x
            current += nums[right]
            # if larger, move `left` to left
            while current > total-x and left <= right:
                current -= nums[left]
                left += 1
            # check if equal
            if current == total-x:
                maxi = max(maxi, right-left+1)

        return n-maxi if maxi != -1 else -1


if __name__ == '__main__':
    main()
