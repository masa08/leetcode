def main():
    args = 10
    solution = Solution()
    result = solution.guessNumber(args)
    print(result)


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# pickが6の場合で考える
def guess(num: int) -> int:
    if num == 6:
        return 0
    elif num > 6:
        return -1
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        def _guessNumber(self, start, end):
            pivod = (start + end) // 2
            result = guess(pivod)

            if result == -1:
                return _guessNumber(self, start, pivod-1)
            elif result == 1:
                return _guessNumber(self, pivod+1, end)
            else:
                return pivod

        return _guessNumber(self, 0, n)


if __name__ == '__main__':
    main()
