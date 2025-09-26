from utils.make_linked_list import makeLinkedList
from utils.linked_list_to_list import linkedListToList
from model import ListNode
from typing import Optional


def main():
    solution = Solution()

    # Simple test: [1,2,3,4,5], remove 2nd from end
    head = makeLinkedList([1, 2, 3, 4, 5])
    result = solution.removeNthFromEnd(head, 2)

    # Print result: should be [1,2,3,5]
    print(linkedListToList(result))


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointers: fast moves n steps ahead first
        slow = fast = head
        for i in range(n):
            fast = fast.next

        # If fast is None, we're removing the first node
        if not fast:
            return head.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return head


if __name__ == '__main__':
    main()
