from typing import Optional
from model.list_node import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists using iterative approach.

        Time Complexity: O(n + m) where n and m are lengths of list1 and list2
        Space Complexity: O(1) - only using dummy node

        Pattern: Two Pointers (on two separate lists)
        """
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.value <= list2.value:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next


def main():
    solution = Solution()

    # Test case 1: Basic merge
    list1 = ListNode.from_list([1, 2, 4])
    list2 = ListNode.from_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    # Verify: [1,1,2,3,4,4]
    assert result.value == 1 and result.next.value == 1

    # Test case 2: Both empty
    list1 = None
    list2 = None
    result = solution.mergeTwoLists(list1, list2)
    assert result is None

    # Test case 3: One empty list
    list1 = None
    list2 = ListNode.from_list([0])
    result = solution.mergeTwoLists(list1, list2)
    assert result.value == 0

    # Test case 4: Different lengths
    list1 = ListNode.from_list([1, 3, 5, 7])
    list2 = ListNode.from_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    assert result.value == 1 and result.next.value == 2

    # Test case 5: All elements in list1 smaller
    list1 = ListNode.from_list([1, 2, 3])
    list2 = ListNode.from_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    assert result.value == 1

    print("All tests passed!")


if __name__ == "__main__":
    main()
