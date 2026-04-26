from typing import List, Optional

from model import TreeNode


def main():
    solution = Solution()

    # Basic case
    root1 = solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert root1.val == 3
    assert root1.left.val == 9
    assert root1.right.val == 20
    assert root1.right.left.val == 15
    assert root1.right.right.val == 7

    # Edge cases
    root2 = solution.buildTree([1], [1])
    assert root2.val == 1
    assert root2.left is None
    assert root2.right is None

    root3 = solution.buildTree([1, 2], [2, 1])
    assert root3.val == 1
    assert root3.left.val == 2

    print("All tests passed!")


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Recursive: preorder[0] is always the root.
        Find root's position in inorder to split left/right subtrees.
        Use that size to split preorder as well.

        Time: O(n^2) - index() is O(n) at each level
        Space: O(n) - recursion depth + array slicing
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


if __name__ == '__main__':
    main()
