class ListNode(object):
    """Node class for a linked list."""

    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next

    @staticmethod
    def from_list(list: list) -> "ListNode":
        dummy = ListNode(0)
        current = dummy
        for value in list:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
