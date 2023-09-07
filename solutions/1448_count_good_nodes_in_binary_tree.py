def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # nodeの最大値を保持しつつ、DFSを行う関数を定義し、条件に合う場合、countを+1する
        def _goodNodes(self, root: TreeNode, count: int, maxval: int) -> int:
            if root is None:
                return count

            if root.val >= maxval:
                count += 1
                maxval = root.val

            if root.left:
                count += _goodNodes(self, root.left, 0, maxval)
            if root.right:
                count += _goodNodes(self, root.right, 0, maxval)

            return count

        res = _goodNodes(self, root, 0, -float('inf'))
        return res


if __name__ == '__main__':
    main()
