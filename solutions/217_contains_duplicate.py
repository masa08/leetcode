from typing import List


def main():
    args = [1, 1, 2, 3]
    solution = Solution()
    result = solution.containsDuplicate(args)
    print(result)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = {}
        for num in nums:
            if num in mapping:
                return True
            else:
                mapping[num] = 1

        return False


if __name__ == '__main__':
    main()
