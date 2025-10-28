
from model import TreeNode
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Check if two binary trees are the same.

        Approach: DFS (Recursive)
        - If both nodes are None, they are the same
        - If one is None and the other is not, they are different
        - If both exist, check if values are equal and recursively check subtrees

        Time Complexity: O(min(n, m)) where n and m are the number of nodes
        Space Complexity: O(min(h1, h2)) for recursion stack, where h1 and h2 are heights
        """
        # Both trees are empty
        if not p and not q:
            return True

        # One tree is empty, the other is not
        if not p or not q:
            return False

        # Both nodes exist - check value and recurse on subtrees
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def main():
    solution = Solution()

    # Test case 1: Same trees [1,2,3]
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)

    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    assert solution.isSameTree(p1, q1) == True, "Test case 1 failed"

    # Test case 2: Different structure [1,2] vs [1,null,2]
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    assert solution.isSameTree(p2, q2) == False, "Test case 2 failed"

    # Test case 3: Different values [1,2,1] vs [1,1,2]
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)

    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)

    assert solution.isSameTree(p3, q3) == False, "Test case 3 failed"

    # Test case 4: Both empty trees
    assert solution.isSameTree(None, None) == True, "Test case 4 failed"

    # Test case 5: One empty, one not
    p5 = TreeNode(1)
    assert solution.isSameTree(p5, None) == False, "Test case 5 failed"
    assert solution.isSameTree(None, p5) == False, "Test case 5 failed"

    # Test case 6: Single node, same value
    p6 = TreeNode(1)
    q6 = TreeNode(1)
    assert solution.isSameTree(p6, q6) == True, "Test case 6 failed"

    # Test case 7: Single node, different value
    p7 = TreeNode(1)
    q7 = TreeNode(2)
    assert solution.isSameTree(p7, q7) == False, "Test case 7 failed"

    print("All tests passed!")


if __name__ == "__main__":
    main()
