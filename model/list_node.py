class ListNode(object):
    """Node class for a linked list."""

    def __init__(self, value=0, next=None) -> None:
        self.value = value
        self.next = next


class DoublyListNode:
    """Node class for a doubly linked list."""

    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None
