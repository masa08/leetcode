def main():
    params = [100, 80, 60, 70, 60, 75, 85]
    obj = StockSpanner()
    for param in params:
        result = obj.next(param)
        print(result)


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            _, prev_span = self.stack.pop()
            span += prev_span

        self.stack.append([price, span])

        return span


if __name__ == '__main__':
    main()
