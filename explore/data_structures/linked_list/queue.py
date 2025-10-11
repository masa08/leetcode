from typing import Any, Optional
from collections import deque


class Node:
    """Node for linked list implementation"""
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional['Node'] = None


class Queue:
    """Queue implementation using linked list
    Time: enqueue O(1), dequeue O(1)
    Space: O(n)
    """
    def __init__(self) -> None:
        self.front: Optional[Node] = None
        self.back: Optional[Node] = None
        self.count: int = 0

    def enqueue(self, item: Any) -> None:
        """Add item to the back of the queue"""
        new_node: Node = Node(item)

        if self.is_empty():
            self.front = self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

        self.count += 1

    def dequeue(self) -> Any:
        """Remove and return item from the front of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        temp_data: Any = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.back = None

        self.count -= 1
        return temp_data

    def empty(self) -> bool:
        """Check if queue is empty"""
        return self.front is None

    def size(self) -> int:
        """Return the number of items in the queue"""
        return self.count

    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return self.front is None


class DequeQueue:
    """Queue implementation using collections.deque
    Time: enqueue O(1), dequeue O(1)
    Space: O(n)
    """

    def __init__(self) -> None:
        self.q: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Add item to the back of the queue"""
        self.q.append(item)

    def dequeue(self) -> Any:
        """Remove and return item from the front of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.q.popleft()

    def empty(self) -> bool:
        """Check if queue is empty"""
        return len(self.q) == 0

    def size(self) -> int:
        """Return the number of items in the queue"""
        return len(self.q)

    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return len(self.q) == 0


def main() -> None:

    q: Queue = Queue()
    assert q.empty() is True
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.size() == 1
    assert q.empty() is False
    q.dequeue()
    assert q.empty() is True

    dq: DequeQueue = DequeQueue()
    assert dq.empty() is True
    dq.enqueue(1)
    dq.enqueue(2)
    dq.enqueue(3)
    assert dq.size() == 3
    assert dq.dequeue() == 1
    assert dq.dequeue() == 2
    assert dq.size() == 1
    assert dq.empty() is False
    dq.dequeue()
    assert dq.empty() is True

    print("All tests passed!")


if __name__ == "__main__":
    main()
