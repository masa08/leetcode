from typing import List


def main():
    args = [1, 2, 3, 4]
    solution = Solution()
    result = solution.distanceBetweenBusStops(args, 0, 1)
    print(result)


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s, e = min(start, destination), max(start, destination)
        first = sum(distance[s:e])
        second = sum(distance) - sum(distance[s:e])

        return min(first, second)


if __name__ == '__main__':
    main()
