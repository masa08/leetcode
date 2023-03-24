def main():
    args = 5
    solution = Solution()
    result = solution.hasAlternatingBits(args)
    print(result)


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)
        prev = binary[2]

        for i in range(3, len(binary)):
            if prev == binary[i]:
                return False
            prev = binary[i]

        return True


if __name__ == '__main__':
    main()
