from typing import List


def main():
    args = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
    solution = Solution()
    result = solution.equalPairs(args)
    print(result)


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if (n == 1):
            return 1

        result = 0
        row_counter = dict()

        for row in range(n):
            row_tuple = tuple(grid[row])
            if row_tuple in row_counter:
                row_counter[row_tuple] += 1
            else:
                row_counter[row_tuple] = 1

        for col in range(n):
            col_tuple = tuple(grid[row][col] for row in range(n))
            if col_tuple in row_counter:
                result += row_counter[col_tuple]

        return result


if __name__ == '__main__':
    main()
