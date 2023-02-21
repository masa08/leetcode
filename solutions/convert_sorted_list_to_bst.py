from typing import Optional, List


def main():
    args = [-3, -1, 0, 2, 4]
    solution = Solution()
    result = solution.sortedArrayToBST(args)
    print(result)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # basecase
        if not nums:
            return None

        left, right = 0, len(nums)-1
        mid = (left + right) // 2
        target = TreeNode(nums[mid])

        target.left = self.sortedArrayToBST(nums[:mid])
        target.right = self.sortedArrayToBST(nums[mid+1:])

        return target


if __name__ == '__main__':
    main()
