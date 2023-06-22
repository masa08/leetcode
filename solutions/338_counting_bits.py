from typing import List


def main():
    args = 2
    solution = Solution()
    result = solution.countBits(args)
    print(result)


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            binary = bin(i)[2:]
            count = binary.count("1")
            ans.append(count)

        return ans


if __name__ == '__main__':
    main()
