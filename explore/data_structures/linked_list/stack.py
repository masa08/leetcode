"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        deleted_element = self.head
        self.head = self.head.next if self.head.next else None
        return deleted_element


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        if self.ll.head == None:
            return None
        return self.ll.delete_first()

    def peak(self):
        "Return the top of the stack"
        return self.ll.head.value if self.ll.head else None


# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)

# Test peak functionality
print("Testing peak():")
print(f"Peak value (should be 3): {stack.peak()}")
print(f"Peak again (should still be 3): {stack.peak()}")

# Test pop functionality
print("\nTesting pop():")
print(f"Pop value (should be 3): {stack.pop().value}")
print(f"Pop value (should be 2): {stack.pop().value}")
print(f"Pop value (should be 1): {stack.pop().value}")
print(f"Pop from empty (should be None): {stack.pop()}")

# Test peak on empty stack
print("\nTesting peak() on empty stack:")
print(f"Peak on empty stack (should be None): {stack.peak()}")

# Push and peak again
stack.push(e4)
print(f"\nAfter pushing 4, peak (should be 4): {stack.peak()}")
print(f"Pop value (should be 4): {stack.pop().value}")
