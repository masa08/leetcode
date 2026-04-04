"""
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Time Complexity: O(1) for both get and put
Space Complexity: O(capacity)

Pattern: Hash Map + Doubly Linked List
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self._remove_from_list(node)
        self._add_to_list(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            old_node = self.key_to_node[key]
            self._remove_from_list(old_node)
            del self.key_to_node[key]

        if len(self.key_to_node) >= self.capacity:
            node_to_delete = self.head.next
            self._remove_from_list(node_to_delete)
            del self.key_to_node[node_to_delete.key]

        node = Node(key, value)
        self.key_to_node[key] = node
        self._add_to_list(node)

    def _add_to_list(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def _remove_from_list(self, node):
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
