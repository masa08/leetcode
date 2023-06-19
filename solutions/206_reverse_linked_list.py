from typing import Optional


def makeLinkedList(arr):
    result = copy = ListNode(arr[0])
    for i in range(1, len(arr)):
        copy.next = ListNode(arr[i])
        copy = copy.next

    return result


def main():
    args = makeLinkedList([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.reverseList(args)
    print(result)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
