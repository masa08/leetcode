def main():
    # 基本的なテストケース
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2

    # エッジケース: 同じ最小値が複数ある場合
    minStack2 = MinStack()
    minStack2.push(0)
    minStack2.push(1)
    minStack2.push(0)
    assert minStack2.getMin() == 0
    minStack2.pop()
    assert minStack2.getMin() == 0

    # エッジケース: 単一要素
    minStack3 = MinStack()
    minStack3.push(5)
    assert minStack3.top() == 5
    assert minStack3.getMin() == 5

    print("All tests passed!")


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        v = self.stack.pop()
        if self.min_stack[-1] == v:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    main()
