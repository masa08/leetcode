import math
from typing import Optional
from utils.make_linked_list import makeLinkedList
from utils.linked_list_to_list import linkedListToList


def main():
    solution = Solution()

    # Test case 1: [1,3,4,7,1,2,6] -> [1,3,4,1,2,6]
    args1 = [1, 3, 4, 7, 1, 2, 6]
    assert linkedListToList(solution.deleteMiddle(
        makeLinkedList(args1))) == [1, 3, 4, 1, 2, 6]

    # Test case 2: [1,2,3,4] -> [1,2,4]
    args2 = [1, 2, 3, 4]
    assert linkedListToList(solution.deleteMiddle(
        makeLinkedList(args2))) == [1, 2, 4]

    # Test case 3: [2,1] -> [2]
    args3 = [2, 1]
    assert linkedListToList(
        solution.deleteMiddle(makeLinkedList(args3))) == [2]

    # Test case 4: [1] -> []
    args4 = [1]
    assert solution.deleteMiddle(makeLinkedList(args4)) is None

    print("All tests passed!")


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Explanation:
        - First pass: Count total nodes
        - Edge case: If only 1 node, return None
        - Calculate middle index (count // 2)
        - Second pass: Traverse to middle-1 and delete middle node

        Time complexity: O(n) - Two passes through the list
        Space complexity: O(1) - Only using pointers

        Pattern: Two-pass linked list traversal
        """
        dummy = head
        count = 0
        while dummy != None:
            dummy = dummy.next
            count += 1

        if count == 1:
            return None

        delete_index = math.floor(count / 2)

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

        return head

        """
        Optimized approach using Fast & Slow pointers:

        Explanation:
        - Use two pointers: slow moves 1 step, fast moves 2 steps
        - When fast reaches end, slow is at middle-1
        - Delete slow.next (middle node)

        Time complexity: O(n) - Single pass
        Space complexity: O(1) - Only using pointers

        Pattern: Fast & Slow pointers (Floyd's algorithm variant)
        """
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
