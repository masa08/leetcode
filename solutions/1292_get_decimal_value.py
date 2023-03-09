def main():
    args = makeLinkedList([1, 0, 1])
    solution = Solution()
    result = solution.getDecimalValue(args)
    print(result)


# Definition for singly-linked list.
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


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binaryString = ""

        while head:
            binaryString += str(head.val)
            head = head.next

        return int(binaryString, 2)


if __name__ == '__main__':
    main()
