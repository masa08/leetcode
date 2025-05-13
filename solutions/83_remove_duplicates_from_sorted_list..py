from typing import Optional
from model import ListNode
from utils import makeLinkedList
from utils import printLinkedListValue


def main():
    args = makeLinkedList([1, 1, 2])
    solution = Solution()
    result = solution.deleteDuplicates(args)
    printLinkedListValue(result)


class Solution:
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current_node = head

    #     while current_node:
    #         while current_node.next and current_node.val == current_node.next.val:
    #             current_node.next = current_node.next.next
    #         current_node = current_node.next

    #     return head

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        prev = head
        current = head.next

        while current:
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                prev = prev.next
                current = current.next

        return head


if __name__ == '__main__':
    main()
