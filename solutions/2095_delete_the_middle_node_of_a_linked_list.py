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


if __name__ == '__main__':
    main()
