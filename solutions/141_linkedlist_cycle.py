from typing import Optional

from common.list_node import ListNode


def makeLinkedList(arr):
    result = copy = ListNode(arr[0])
    for i in range(1, len(arr)):
        copy.next = ListNode(arr[i])
        copy = copy.next
    # To make cycle
    copy.next = result.next.next

    return result


def main():
    args = makeLinkedList([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.hasCycle(args)
    print(result)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Hash Table
        # seen = set()

        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next

        # return False

        # Floyd's Cycle Finding Algorithm
        if head is None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


if __name__ == '__main__':
    main()
