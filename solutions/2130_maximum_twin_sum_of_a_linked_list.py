from typing import Optional


def main():
    solution = Solution()

    # Basic case: [5,4,2,1]
    head1 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    assert solution.pairSum(head1) == 6

    # Basic case: [4,2,2,3]
    head2 = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
    assert solution.pairSum(head2) == 7

    # Minimum case: [1,2]
    head3 = ListNode(1, ListNode(2))
    assert solution.pairSum(head3) == 3

    print("All tests passed!")


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Approach: Stack-based twin sum calculation
        - Store all node values in a stack
        - Iterate first half of list, popping from stack to get twin pairs
        - Track maximum twin sum

        Time Complexity: O(n) - traverse list twice
        Space Complexity: O(n) - stack stores all node values
        """
        # initialize stack
        curr = head
        stack = []
        while curr:
            stack.append(curr.val)
            curr = curr.next

        # iterate first half of list
        size = len(stack)
        count = 1
        maximum = 0
        while count <= size/2:
            maximum = max(maximum, head.val + stack.pop())
            head = head.next
            count += 1

        return maximum

    def pairSum_twoPointer(self, head: Optional[ListNode]) -> int:
        """
        Approach: Two Pointer (Fast/Slow) + Reverse second half
        - Use fast/slow pointers to find middle of list
        - Reverse the second half of the list
        - Traverse both halves simultaneously to calculate twin sums

        Time Complexity: O(n) - traverse list multiple times
        Space Complexity: O(1) - only constant extra space
        """
        # Find middle using fast/slow pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Calculate maximum twin sum
        maximum = 0
        first, second = head, prev
        while second:
            maximum = max(maximum, first.val + second.val)
            first = first.next
            second = second.next

        return maximum


if __name__ == '__main__':
    main()
