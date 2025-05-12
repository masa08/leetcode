def main():
    solution = Solution()
    result = solution.hammingDistance(1, 4)

    print(result)


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")


if __name__ == "__main__":
    main()
