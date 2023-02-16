import math


def main():
    args = 5
    solution = Solution()
    result = solution.countTriples(args)
    print(result)


class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                target = math.sqrt(i**2 + j**2)
                if target % 1 == 0 and target <= n:
                    count += 2

        return count


if __name__ == '__main__':
    main()
