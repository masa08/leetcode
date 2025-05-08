from typing import Optional

from model import ListNode
from utils import makeLinkedList, printLinkedListValue


def main():
    args = makeLinkedList([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.reverseList(args)
    printLinkedListValue(result)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None

        while head:
            next_nodes = head.next
            head.next = result
            result = head
            head = next_nodes

        return result


if __name__ == '__main__':
    main()
