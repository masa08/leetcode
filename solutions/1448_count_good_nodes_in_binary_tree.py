from model import TreeNode


def main():
    # Create test data: Binary tree
    # Example tree:
    #        3
    #       / \
    #      1   4
    #     /   / \
    #    3   1   5
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    solution = Solution()
    result = solution.goodNodes(root)

    print(f"Number of good nodes: {result}")


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # nodeの最大値を保持しつつ、DFSを行う関数を定義し、条件に合う場合、countを+1する
        def _goodNodes(root: TreeNode, count: int, maxval: int) -> int:
            if root is None:
                return count

            if root.val >= maxval:
                count += 1
                maxval = root.val

            count += _goodNodes(root.left, 0, maxval)
            count += _goodNodes(root.right, 0, maxval)

            return count

        res = _goodNodes(root, 0, -float('inf'))
        return res


if __name__ == '__main__':
    main()
