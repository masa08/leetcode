from typing import List


def main():
    args = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    solution = Solution()
    result = solution.equalPairs(args)
    print(result)


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        row_counter = dict()

        for row in range(n):
            target = tuple(grid[row])
            if target in row_counter:
                row_counter[target] += 1
            else:
                row_counter[target] = 1

        for c in range(n):
            col = [grid[i][c] for i in range(n)]
            if tuple(col) in row_counter:
                count += row_counter[tuple(col)]

        return count


if __name__ == '__main__':
    main()
