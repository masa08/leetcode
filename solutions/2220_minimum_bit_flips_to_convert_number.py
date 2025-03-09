def main():
    args = [3, 4]
    solution = Solution()
    result = solution.minBitFlips(*args)
    print(result)


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0

        while start > 0 or goal > 0:
            if (start & 1) != (goal & 1):
                count += 1
            start >>= 1
            goal >>= 1

        return count


if __name__ == '__main__':
    main()
