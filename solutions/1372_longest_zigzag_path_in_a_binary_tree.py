def main():
    args = [1, 7, 0, 7, -8, None, None]
    solution = Solution()
    result = solution.longestZigZag(args)
    print(result)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root) -> int:
        self.max_length = 0

        def dfs(node, next_direction, length):
            if not node:
                return

            self.max_length = max(self.max_length, length)

            if next_direction == "left":
                dfs(node.left, "right", length + 1)
                dfs(node.right, "left", 1)
            else:
                dfs(node.right, "left", length + 1)
                dfs(node.left, "right", 1)

        dfs(root.left, "right", 1)
        dfs(root.right, "left", 1)

        return self.max_length


if __name__ == '__main__':
    main()
