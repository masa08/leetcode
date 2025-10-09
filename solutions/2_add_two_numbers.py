from typing import Optional

from model import ListNode
from utils import makeLinkedList, printLinkedListValue, linkedListToList


def main():
    solution = Solution()

    # 基本ケース: 342 + 465 = 807
    l1 = makeLinkedList([2, 4, 3])
    l2 = makeLinkedList([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedListToList(result) == [7, 0, 8]

    # エッジケース: 0 + 0 = 0
    l1 = makeLinkedList([0])
    l2 = makeLinkedList([0])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedListToList(result) == [0]

    # 桁上がりケース: 9999999 + 9999 = 10009998
    l1 = makeLinkedList([9, 9, 9, 9, 9, 9, 9])
    l2 = makeLinkedList([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    assert linkedListToList(result) == [8, 9, 9, 9, 0, 0, 0, 1]

    print("All tests passed!")


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as linked lists in reverse order.

        Algorithm: Simulate digit-by-digit addition with carry handling
        - Traverse both lists simultaneously
        - Add corresponding digits and carry from previous step
        - Create new node for each digit sum (mod 10)
        - Continue until both lists exhausted and no carry remains

        Time Complexity: O(max(m, n)) where m and n are lengths of l1 and l2
        Space Complexity: O(max(m, n)) for the result linked list

        Pattern: Two Pointers (simultaneous traversal)
        """
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.value if l1 else 0
            value2 = l2.value if l2 else 0
            total = value1 + value2 + carry

            if total >= 10:
                carry = 1
                total %= 10
            else:
                carry = 0

            current.next = ListNode(total)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


if __name__ == '__main__':
    main()
