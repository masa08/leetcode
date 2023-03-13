def main():
    args = 5
    solution = Solution()
    result = solution.findComplement(args)
    print(result)


class Solution:
    def findComplement(self, num: int) -> int:
        todo, bit = num, 1

        while todo > 0:
            num = num ^ bit

            bit = bit << 1  # change target bit
            todo = todo >> 1  # bitの長さをこれで測る

        return num


if __name__ == '__main__':
    main()
