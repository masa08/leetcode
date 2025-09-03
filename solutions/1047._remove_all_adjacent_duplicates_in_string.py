def main():
    solution = Solution()

    # 基本ケース
    assert solution.removeDuplicates("abbaca") == "ca"
    assert solution.removeDuplicates("azxxzy") == "ay"

    # エッジケース
    assert solution.removeDuplicates("") == ""
    assert solution.removeDuplicates("a") == "a"
    assert solution.removeDuplicates("aa") == ""
    assert solution.removeDuplicates("aaa") == "a"

    # 連続削除
    assert solution.removeDuplicates("aaaa") == ""
    assert solution.removeDuplicates("abba") == ""

    print("All tests passed!")


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
                continue

            stack.append(c)

        return "".join(stack)


if __name__ == '__main__':
    main()
