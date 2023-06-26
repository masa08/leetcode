def main():
    args = "ab**c"
    solution = Solution()
    result = solution.removeStars(args)
    print(result)


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            char = s[i]
            if char != "*":
                stack.append(char)
                continue

            stack.pop()

        return "".join(stack)


if __name__ == '__main__':
    main()
