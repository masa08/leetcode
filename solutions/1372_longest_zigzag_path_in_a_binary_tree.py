from utils import makeBinarySearchTree


def main():
    # Convert array to binary tree
    args = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
    root = makeBinarySearchTree(args)  # 配列を二分木に変換
    # Solve the problem
    solution = Solution()
    result = solution.longestZigZag(root)
    print(result)


class Solution:
    def longestZigZag(self, root) -> int:
        self.max_length = 0

        def dfs(node, next_direction, zigzag_length):
            if not node:
                return

            self.max_length = max(self.max_length, zigzag_length)

            if next_direction == "left":
                dfs(node.left, "right", zigzag_length + 1)
                dfs(node.right, "left", 1)
            else:
                dfs(node.right, "left", zigzag_length + 1)
                dfs(node.left, "right", 1)

        dfs(root.left, "right", 1)
        dfs(root.right, "left", 1)

        return self.max_length


if __name__ == '__main__':
    main()
