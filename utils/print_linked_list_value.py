from model import ListNode


def printLinkedListValue(node: ListNode):
    while node:
        print(node.val)
        node = node.next
