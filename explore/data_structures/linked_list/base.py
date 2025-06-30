class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # for check a value of each node.
    def print(self) -> None:
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, new_element) -> None:
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position) -> Node:
        current = self.head
        index = 1
        while current:
            if index == position:
                return current
            current = current.next
            index += 1
        return None

    def insert(self, new_element, position) -> None:
        prev = self.head
        current = prev.next
        if position == 1:
            new_element.next = prev
            self.head = new_element
            return

        index = 2
        while current:
            if index == position:
                prev.next = new_element
                new_element.next = current
                return
            prev = prev.next
            current = current.next
            index += 1

    def delete(self, value):
        prev = self.head
        current = prev.next

        if prev.value == value:
            self.head = current
            return

        while current:
            if current.value == value:
                prev.next = current.next
                self.head = prev
                return
            current = current.next


# Test cases
# Set up some Elements
# 1 => 2 => 3 => 4
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)


# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)
# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
