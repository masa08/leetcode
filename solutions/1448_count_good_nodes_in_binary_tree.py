from model import TreeNode
from collections import deque


def main():
    solution_dfs = SolutionDFS()
    solution_bfs = SolutionBFS()

    # Test case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.right.left = TreeNode(1)
    root1.right.right = TreeNode(5)
    assert solution_dfs.goodNodes(root1) == 4
    assert solution_bfs.goodNodes(root1) == 4

    # Test case 2
    root2 = TreeNode(3)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(2)
    assert solution_dfs.goodNodes(root2) == 3
    assert solution_bfs.goodNodes(root2) == 3

    # Test case 3: single node
    root3 = TreeNode(1)
    assert solution_dfs.goodNodes(root3) == 1
    assert solution_bfs.goodNodes(root3) == 1

    print("All tests passed!")


class SolutionDFS:
    """
    DFS (Depth-First Search) implementation

    Time Complexity: O(n) - Visit each node once
    Space Complexity: O(h) - Recursion stack (h = tree height, worst O(n))
    """

    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, path_max: int) -> int:
            if not node:
                return 0

            # Count current node if it's a good node
            is_good_node = node.val >= path_max
            current_count = 1 if is_good_node else 0

            # Update max for children
            new_max = max(path_max, node.val)

            # Recursively count good nodes in subtrees
            left_count = dfs(node.left, new_max)
            right_count = dfs(node.right, new_max)

            return current_count + left_count + right_count

        return dfs(root, float('-inf'))


class SolutionBFS:
    """
    BFS (Breadth-First Search) implementation

    Algorithm:
    - Store (node, max_val) pairs in queue
    - Visit nodes level by level and increment count if node.val >= max_val
    - Pass updated max_val to children when adding to queue

    Time Complexity: O(n) - Visit each node once
    Space Complexity: O(w) - Queue size (w = max tree width, worst case O(n))
    """

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        count = 0
        queue = deque([(root, float('-inf'))])

        while queue:
            node, max_val = queue.popleft()

            # Check if current node is a good node
            if node.val >= max_val:
                count += 1

            # Update max value for next level
            new_max = max(max_val, node.val)

            if node.left:
                queue.append((node.left, new_max))
            if node.right:
                queue.append((node.right, new_max))

        return count


# LeetCode submission用
Solution = SolutionDFS


if __name__ == '__main__':
    main()
