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
        Approach 1: Hash Table

        Explanation:
        - Store visited nodes in a set
        - If we encounter a node already in the set, there's a cycle
        - If we reach None, no cycle exists

        Time complexity: O(n) - Visit each node once
        Space complexity: O(n) - Store all nodes in set

        Pattern: Hash Table for cycle detection
        """
        # seen = set()

        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next

        # return False

        """
        Approach 2: Floyd's Cycle Finding Algorithm (Tortoise and Hare)

        Explanation:
        - Use two pointers: slow moves 1 step, fast moves 2 steps
        - If there's a cycle, fast will eventually catch up to slow
        - If fast reaches None, no cycle exists

        Time complexity: O(n) - Fast pointer travels at most 2n steps
        Space complexity: O(1) - Only using two pointers

        Pattern: Fast & Slow pointers (Floyd's algorithm)
        """
        if head is None:
            return False
        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


if __name__ == '__main__':
    main()
