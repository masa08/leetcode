from typing import List


def main():
    args = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    result = solution.maxArea(args)
    print(result)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            maxarea = max(maxarea, area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxarea


if __name__ == '__main__':
    main()
