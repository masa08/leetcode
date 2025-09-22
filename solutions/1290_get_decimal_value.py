from model import ListNode
from utils import makeLinkedList


def main():
    solution = Solution()

    # 基本ケース
    assert solution.getDecimalValue(makeLinkedList([1, 0, 1])) == 5  # 101 = 5
    assert solution.getDecimalValue(makeLinkedList([0])) == 0
    assert solution.getDecimalValue(makeLinkedList([1])) == 1

    # エッジケース
    assert solution.getDecimalValue(makeLinkedList(
        [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) == 18880

    print("All tests passed!")


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # binaryString = ""

        # while head:
        #     binaryString += str(head.value)
        #     head = head.next

        # return int(binaryString, 2)

        num = head.value
        while head.next:
            # Shift left by 1 (multiply by 2) and add next bit
            num = (num << 1) | head.next.value
            head = head.next
        return num


if __name__ == '__main__':
    main()
