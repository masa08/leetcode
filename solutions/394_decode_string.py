def main():
    args = "3[a2[c]]"
    solution = Solution()
    result = solution.decodeString(args)
    print(result)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0

        while i < len(s):
            if s[i] == ']':
                decoded_string = []
                # get the encoded string
                while stack[-1] != '[':
                    decoded_string.append(stack.pop())
                # pop [ from the stack
                stack.pop()

                base = 1
                k = 0
                # get the number k
                while stack and stack[-1].isdigit():
                    k = int(stack.pop()) * base + k
                    base *= 10

                # decode k[decodedString], by pushing decodedString k times into stack
                while k != 0:
                    for j in range(len(decoded_string)-1, -1, -1):
                        stack.append(decoded_string[j])
                    k -= 1
            else:
                # push the current character to stack
                stack.append(s[i])
            i += 1

        # get the result from stack
        return ''.join(stack)


if __name__ == '__main__':
    main()
