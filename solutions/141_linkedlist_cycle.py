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
        seen = set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False


if __name__ == '__main__':
    main()
