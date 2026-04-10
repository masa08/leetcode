def main():
    solution = Solution()

    # Basic cases
    assert solution.isValid("()") is True
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("{[]}") is True

    # Edge cases
    assert solution.isValid("(]") is False        # Mismatched pair
    assert solution.isValid("([)]") is False       # Wrong nesting order
    # Closing bracket with empty stack
    assert solution.isValid(")") is False
    assert solution.isValid("(") is False          # Unclosed bracket

    print("All tests passed!")


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Use a stack to match opening and closing brackets.
        Push opening brackets, pop on matching closing brackets.
        If a closing bracket doesn't match the top of stack, it's invalid.

        Time: O(n) - single pass through the string
        Space: O(n) - stack stores opening brackets
        """
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping:
                # Closing bracket: must match the most recent opening bracket
                top = stack[-1] if stack else None
                if top == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0


if __name__ == "__main__":
    main()
