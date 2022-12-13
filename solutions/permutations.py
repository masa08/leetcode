from typing import List


def main():
    args = [1, 2, 3]
    solution = Solution()
    result = solution.permute(args)
    print(result)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        self.backtracking(res, visited, [], nums)
        return res

    def backtracking(self, res, visited, subset, nums):
        if len(subset) == len(nums):
            res.append(subset)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.backtracking(res, visited, subset+[nums[i]], nums)
                visited.remove(i)


if __name__ == '__main__':
    main()
