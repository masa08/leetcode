from typing import Optional
from model.list_node import ListNode
from utils.make_linked_list import makeLinkedList
from utils.linked_list_to_list import linkedListToList


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy

        while cur.next:
            if cur.next.value == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

        # if head is None: return head

        # curr = head
        # while head and head.next:
        #     if head.next.val == val:
        #         head.next = head.next.next
        #     else:
        #         head = head.next

        # return curr.next if curr.val == val else curr


def main():
    solution = Solution()

    # Test case 1: Remove middle and end nodes
    head1 = makeLinkedList([1, 2, 6, 3, 4, 5, 6])
    result1 = solution.removeElements(head1, 6)
    assert linkedListToList(result1) == [1, 2, 3, 4, 5]

    # Test case 2: Empty list
    head2 = None
    result2 = solution.removeElements(head2, 1)
    assert result2 is None

    # Test case 3: Remove all nodes
    head3 = makeLinkedList([7, 7, 7, 7])
    result3 = solution.removeElements(head3, 7)
    assert result3 is None

    # Test case 4: Remove head node
    head4 = makeLinkedList([1, 1, 2, 3])
    result4 = solution.removeElements(head4, 1)
    assert linkedListToList(result4) == [2, 3]

    # Test case 5: Single node (remove)
    head5 = makeLinkedList([1])
    result5 = solution.removeElements(head5, 1)
    assert result5 is None

    # Test case 6: Single node (keep)
    head6 = makeLinkedList([1])
    result6 = solution.removeElements(head6, 2)
    assert linkedListToList(result6) == [1]

    print("All tests passed!")


if __name__ == "__main__":
    main()
