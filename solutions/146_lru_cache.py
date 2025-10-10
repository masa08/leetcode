"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)

Pattern: Hash Map + Doubly Linked List
"""


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


def main():
    # Basic test
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)
    assert lru.get(2) == -1
    lru.put(4, 4)
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4

    print("All tests passed!")


if __name__ == '__main__':
    main()
