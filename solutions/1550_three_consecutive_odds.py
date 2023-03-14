from typing import List


def main():
    args = [1, 1, 1]
    solution = Solution()
    result = solution.threeConsecutiveOdds(args)
    print(result)


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def _odd(number: int) -> bool:
            return number % 2 == 1

        consectiveNumber = 0
        for i in range(len(arr)):
            if _odd(arr[i]):
                consectiveNumber += 1
            else:
                consectiveNumber = 0
            if consectiveNumber >= 3:
                return True

        return False


if __name__ == '__main__':
    main()
