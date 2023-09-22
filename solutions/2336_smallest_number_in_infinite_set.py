import heapq


def main():
    num = 1
    obj = SmallestInfiniteSet()
    param_1 = obj.popSmallest()
    obj.addBack(num)


class SmallestInfiniteSet:
    def __init__(self):
        self.added_integers = []
        self.current_integer = 1

    def popSmallest(self) -> int:
        if len(self.added_integers):
            smollest = heapq.heappop(self.added_integers)
        else:
            smollest = self.current_integer
            self.current_integer += 1
        return smollest

    def addBack(self, num: int) -> None:
        if self.current_integer <= num or num in self.added_integers:
            return
        else:
            heapq.heappush(self.added_integers, num)


if __name__ == '__main__':
    main()
