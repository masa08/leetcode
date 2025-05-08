from model import ListNode


def printLinkedListValue(node: ListNode):
    while node:
        print(node.value, end=" -> ")
        node = node.next
