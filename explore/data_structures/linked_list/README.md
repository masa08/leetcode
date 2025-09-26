# Linked List

A linear data structure where elements are linked using pointers.

## Core Concept

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Time Complexity

| Operation | Time |
|-----------|------|
| Insert at head | O(1) |
| Delete at head | O(1) |
| Access/Search | O(n) |
| Insert/Delete at position | O(n) |

## Essential Patterns

### Two Pointers (Fast & Slow)

Used for:

- Cycle detection
- Finding middle node
- Finding nth from end

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Dummy Node

Simplifies edge cases in operations like merge and delete.

```python
dummy = ListNode(0)
dummy.next = head
```

### Reversal Pattern

```python
prev, curr = None, head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
```

## Common Problems

1. **Reverse**: Iterative vs Recursive
2. **Cycle Detection**: Floyd's algorithm
3. **Merge**: Two sorted lists
4. **Palindrome**: Fast/slow + reverse
5. **Intersection**: Length difference technique
