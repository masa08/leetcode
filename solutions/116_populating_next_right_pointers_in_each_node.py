from typing import Optional


def main():
    # Create test data: Perfect binary tree
    # Example tree:
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Apply the solution
    solution = Solution()
    result = solution.connect(root)

    # Print the next pointers for each level
    def print_levels(node):
        while node:
            current = node
            while current:
                print(current.val, end=" -> " if current.next else " -> None\n")
                current = current.next
            node = node.left

    print_levels(result)


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None

        queue = [root]
        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.pop(0)

                if i < size - 1:
                    node.next = queue[0]
                else:
                    node.next = None

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


if __name__ == '__main__':
    main()
