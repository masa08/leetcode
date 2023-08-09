from typing import List


def main():
    args = [1, 2, 3, 4, 5]
    solution = Solution()
    result = solution.increasingTriplet(args)
    print(result)


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


if __name__ == '__main__':
    main()
