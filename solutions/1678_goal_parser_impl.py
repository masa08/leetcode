def main():
    args = "G()(al)"
    solution = Solution()
    result = solution.interpret(args)
    print(result)


class Solution:
    def interpret(self, command: str) -> str:
        # return command.replace("()", "o").replace("(al)", "al")
        map = {"G": "G", "()": "o", "(al)": "al"}
        temp = ""
        res = ""

        for c in command:
            temp += c
            if temp in map:
                res += map[temp]
                temp = ""
        return res


if __name__ == '__main__':
    main()
