from collections import defaultdict


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def makeTree(args):
    nodes = [TreeNode(val) if val else None for val in args]
    for i, node in enumerate(nodes):
        if node:
            left = i * 2 + 1
            right = i * 2 + 2
            if left < len(nodes):
                node.left = nodes[left]
            if right < len(nodes):
                node.right = nodes[right]
    return nodes[0]


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
