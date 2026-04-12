from typing import Optional

from model import ListNode


def main():
    solution = Solution()

    # サイクルありケース
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = head1  # サイクル作成
    assert solution.hasCycle(head1) == True

    # サイクルなしケース
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    assert solution.hasCycle(head2) == False

    # エッジケース
    assert solution.hasCycle(None) == False
    assert solution.hasCycle(ListNode(1)) == False

    print("All tests passed!")


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's Cycle Detection (Tortoise and Hare).
        slow moves 1 step, fast moves 2 steps. If there's a cycle,
        fast will eventually catch up to slow (like runners on a track).

        Alternative: Hash Set approach stores visited nodes in a set - O(n) space.
        Floyd's achieves the same result with O(1) space.

        Time: O(n) - fast pointer travels at most 2n steps
        Space: O(1) - only two pointers
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


if __name__ == '__main__':
    main()
