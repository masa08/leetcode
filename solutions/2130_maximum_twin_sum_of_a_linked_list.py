from typing import Optional


def main():
    args = [1, 4, 3, 2]
    solution = Solution()
    result = solution.pairSum(args)
    print(result)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # initialize stack
        curr = head
        stack = []

        while curr:
            stack.append(curr.val)
            curr = curr.next

        # iterate ll
        size = len(stack)
        count = 1
        maximum = 0
        while count <= size/2:
            maximum = max(maximum, head.val + stack.pop())
            head = head.next
            count += 1

        return maximum

        # # get length and store map
        # dummy = head
        # length = 0
        # mapping = {}
        # while dummy:
        #     mapping[length] = dummy.val
        #     length += 1
        #     dummy = dummy.next

        # # iterate ll and update maximum
        # maximum = 0
        # index = 0
        # while head:
        #     maximum = max(head.val + mapping[length-1-index], maximum)
        #     head = head.next
        #     index += 1

        # # return maximun
        # return maximum


if __name__ == '__main__':
    main()
