def main():
    args = "()"
    solution = Solution()
    result = solution.isValid(args)

    print(result)

class Solution:
    def isValid(self, symbles: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for symble in symbles:
            if symble in mapping:
                latest_symble = stack[-1] if len(stack) > 0 else None
                if latest_symble and latest_symble == mapping[symble]:
                    stack.pop()
                else:
                    stack.append(symble)
            else:
                stack.append(symble)

        return len(stack) == 0


if __name__ == "__main__":
    main()
