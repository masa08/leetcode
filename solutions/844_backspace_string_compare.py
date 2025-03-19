def main():
    args = ("ab#c", "ad#c")
    solution = Solution()
    result = solution.backspaceCompare(*args)
    print(result)


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        for char in s:
            if char == "#":
                s_stack.pop() if s_stack else None
            else:
                s_stack.append(char)

        t_stack = []
        for char in t:
            if char == "#":
                t_stack.pop() if t_stack else None
            else:
                t_stack.append(char)
        print(t_stack, s_stack)
        return t_stack == s_stack


if __name__ == '__main__':
    main()
