from typing import Optional
from model import ListNode
from utils import makeLinkedList


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Convert linked list to array and check if it's a palindrome.

        1. Traverse the linked list and store all values in an array
        2. Compare the array with its reverse using Python's slicing

        Time: O(n) - single pass through the list
        Space: O(n) - array to store all values

        Trade-off: Simple and readable, but uses O(n) extra space.
        Could optimize to O(1) space by reversing second half in-place.
        """
        vals = []
        while head:
            vals.append(head.value)
            head = head.next
        return vals == vals[::-1]

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        """
        Approach: Use two pointers to check if the linked list is a palindrome.

        1. Find the middle of the linked list
        2. Reverse the second half of the linked list
        3. Compare the first half with the reversed second half

        Time: O(n) - single pass through the list
        Space: O(1) - no extra space used

        Trade-off: More efficient space-wise, but slightly more complex.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        while prev:
            if prev.value != head.value:
                return False
            prev = prev.next
            head = head.next

        return True


def main():
    solution = Solution()

    # Test case 1: Palindrome (even length)
    head1 = makeLinkedList([1, 2, 2, 1])
    assert solution.isPalindrome(head1) == True
    head1 = makeLinkedList([1, 2, 2, 1])
    assert solution.isPalindrome2(head1) == True

    # Test case 2: Not palindrome
    head2 = makeLinkedList([1, 2])
    assert solution.isPalindrome(head2) == False
    head2 = makeLinkedList([1, 2])
    assert solution.isPalindrome2(head2) == False

    # Test case 3: Single node
    head3 = makeLinkedList([1])
    assert solution.isPalindrome(head3) == True
    head3 = makeLinkedList([1])
    assert solution.isPalindrome2(head3) == True

    print("All tests passed!")


if __name__ == "__main__":
    main()
