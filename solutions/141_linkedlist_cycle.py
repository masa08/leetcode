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
        # Hash Table
        # seen = set()

        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next

        # return False

        # Floyd's Cycle Finding Algorithm
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
