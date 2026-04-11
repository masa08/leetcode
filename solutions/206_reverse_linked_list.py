from typing import Optional

from model import ListNode
from utils import makeLinkedList, linkedListToList


def main():
    solution = Solution()

    # Basic case
    assert linkedListToList(solution.reverseList(
        makeLinkedList([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]

    # Edge cases
    assert solution.reverseList(None) is None  # Empty list
    assert linkedListToList(solution.reverseList(
        makeLinkedList([1]))) == [1]  # Single node
    assert linkedListToList(solution.reverseList(
        makeLinkedList([1, 2]))) == [2, 1]  # Two nodes

    print("All tests passed!")


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iteratively reverse the linked list using three pointers.
        For each node: save next, point current to prev, advance both pointers.

        Time: O(n) - visit each node once
        Space: O(1) - only three pointers
        """
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev


if __name__ == '__main__':
    main()
