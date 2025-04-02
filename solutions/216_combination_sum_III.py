from typing import List


def main():
    solution = Solution()
    result = solution.combinationSum3(3, 9)
    print(result)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(start, path, total):
            if len(path) == k and total == n:
                results.append(path.copy())
            if len(path) >= k or total >= n:
                return

            for i in range(start, 10):
                path.append(i)
                backtrack(i+1, path, total+i)
                path.pop()

        backtrack(1, [], 0)
        return results


if __name__ == '__main__':
    main()
