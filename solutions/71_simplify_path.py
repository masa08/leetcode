def main():
    solution = Solution()

    assert solution.simplifyPath("/home/") == "/home"
    assert solution.simplifyPath("/../") == "/"
    assert solution.simplifyPath("/home//foo/") == "/home/foo"
    assert solution.simplifyPath("/a/./b/../../c/") == "/c"

    print("All tests passed!")


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = [p for p in path.split('/') if p]
        stack = []

        for path in paths:
            if path == '.':
                continue
            elif path == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(path)

        return '/' + '/'.join(stack)


if __name__ == '__main__':
    main()
