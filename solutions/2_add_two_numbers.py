from typing import Optional

from model import ListNode
from utils import makeLinkedList, printLinkedListValue


def linkedListToList(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result


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

        # l1_arr, l2_arr = [], []

        # # node to array
        # while l1:
        #     l1_arr.append(l1.value)
        #     l1 = l1.next
        # while l2:
        #     l2_arr.append(l2.value)
        #     l2 = l2.next

        # reversed_l1_int = int("".join(map(str, l1_arr))[::-1])
        # reversed_l2_int = int("".join(map(str, l2_arr))[::-1])

        # total = reversed_l1_int + reversed_l2_int
        # reversed_total_list = list(str(total))[::-1]

        # result = copy = ListNode(int(reversed_total_list[0]))
        # for digits in range(1, len(reversed_total_list)):
        #     copy.next = ListNode(int(reversed_total_list[digits]))
        #     copy = copy.next

        # return result


if __name__ == '__main__':
    main()
