from collections import defaultdict
from model import TreeNode
from utils import makeTree


def main():
    args = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    args = makeTree(args)
    solution = Solution()
    result = solution.pathSum(args, 8)
    print(result)


class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            count = prefix_sums[current_sum - targetSum]
            prefix_sums[current_sum] += 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            prefix_sums[current_sum] -= 1

            return count

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        return dfs(root, 0)


if __name__ == '__main__':
    main()
