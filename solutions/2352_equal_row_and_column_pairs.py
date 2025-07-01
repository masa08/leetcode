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

        count = 0
        row_counter = dict()

        for row in range(n):
            row_tuple = tuple(grid[row])
            if row_tuple in row_counter:
                row_counter[row_tuple] += 1
            else:
                row_counter[row_tuple] = 1

        for col in range(n):
            col_tuple = tuple(grid[i][col] for i in range(n))
            if col_tuple in row_counter:
                count += row_counter[col_tuple]

        return count


if __name__ == '__main__':
    main()
