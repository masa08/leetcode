import math
from typing import Optional


def main():
    args = ""
    solution = Solution()
    result = solution.hoge()
    print(result)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find target index
        dummy = head
        count = 0
        while dummy != None:
            dummy = dummy.next
            count += 1

        if count == 1:
            return None

        delete_index = math.floor(count / 2)

        # define prev and curr and delete index node
        prev = curr = head
        index = 0

        while curr != None:
            if index == delete_index:
                prev.next = curr.next
                curr = prev.next
                break
            prev = curr
            curr = curr.next
            index += 1

        # return head
        return head

        # another solution1
        # if head.next == None:
        #     return None

        # count = 0
        # p1 = p2 = head

        # while p1:
        #     count += 1
        #     p1 = p1.next

        # middle_index = count // 2

        # for _ in range(middle_index-1):
        #     p2 = p2.next

        # p2.next = p2.next.next

        # return head

        # another solution2
        # if head.next == None:
        #     return None

        # slow, fast = head, head.next.next

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # slow.next = slow.next.next

        # return head


if __name__ == '__main__':
    main()
