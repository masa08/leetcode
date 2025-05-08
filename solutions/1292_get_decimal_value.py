from model import ListNode
from utils import makeLinkedList


def main():
    args = makeLinkedList([1, 0, 1])
    solution = Solution()
    result = solution.getDecimalValue(args)
    print(result)


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binaryString = ""

        while head:
            binaryString += str(head.value)
            head = head.next

        return int(binaryString, 2)


if __name__ == '__main__':
    main()
