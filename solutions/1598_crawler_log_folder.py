from typing import List


def main():
    solution = Solution()

    # テストケース1: 基本的な移動
    assert solution.minOperations(["d1/", "d2/", "../", "d21/", "./"]) == 2

    # テストケース2: ルートより上に戻ろうとする
    assert solution.minOperations(["d1/", "../", "../", "../"]) == 0

    # テストケース3: 現在位置に留まる
    assert solution.minOperations(["./", "../", "./"]) == 0

    print("All tests passed!")


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if log == '../':
                if stack:
                    stack.pop()
            elif log == './':
                continue
            else:
                stack.append(log)

        return len(stack)


if __name__ == '__main__':
    main()
