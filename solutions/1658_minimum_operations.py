def main():
    args = "0100"
    solution = Solution()
    result = solution.minOperations(args)
    print(result)


class Solution:
    def minOperations(self, s: str) -> int:
        length = len(s)

        arrStartFromZero = [0 if i % 2 == 0 else 1 for i in range(length)]
        arrStartFromOne = [1 if i % 2 == 0 else 0 for i in range(length)]

        temp = 0
        temp2 = 0

        for i in range(length):
            target = int(s[i])
            if target != arrStartFromZero[i]:
                temp += 1
            if target != arrStartFromOne[i]:
                temp2 += 1

        return min(temp, temp2)


if __name__ == '__main__':
    main()
