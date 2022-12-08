from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def makeLinkedList(arr):
    result = copy = ListNode(arr[0])
    for i in range(1, len(arr)):
        copy.next = ListNode(arr[i])
        copy = copy.next

    return result


def printLinkedList(node: ListNode):
    while node:
        print(node.val)
        node = node.next


def main():
    args1 = makeLinkedList([2, 4, 3])
    args2 = makeLinkedList([5, 6, 4])
    solution = Solution()
    result = solution.addTwoNumbers(args1, args2)
    printLinkedList(result)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_arr, l2_arr = [], []

        # node to array
        while l1:
            l1_arr.append(l1.val)
            l1 = l1.next
        while l2:
            l2_arr.append(l2.val)
            l2 = l2.next

        reversed_l1_int = int("".join(map(str, l1_arr))[::-1])
        reversed_l2_int = int("".join(map(str, l2_arr))[::-1])

        total = reversed_l1_int + reversed_l2_int
        reversed_total_list = list(str(total))[::-1]

        result = copy = ListNode(int(reversed_total_list[0]))
        for digits in range(1, len(reversed_total_list)):
            copy.next = ListNode(int(reversed_total_list[digits]))
            copy = copy.next

        return result


if __name__ == '__main__':
    main()
