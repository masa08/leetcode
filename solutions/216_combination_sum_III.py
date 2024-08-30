from typing import List


def main():
    solution = Solution()
    result = solution.combinationSum3(3, 9)
    print(result)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        conbinations = []

        def backtrack(start, path, remain):
            if remain == 0 and len(path) == k:
                conbinations.append(list(path))
                return
            elif remain < 0 or len(path) == k:
                return

            for i in range(start, 10):
                path.append(i)
                # Recursively call backtrack with the next number and updated remaining sum
                backtrack(i+1, path, remain - i)
                # Remove the last number from the path to backtrack
                path.pop()

        backtrack(1, [], n)
        return conbinations


if __name__ == '__main__':
    main()
