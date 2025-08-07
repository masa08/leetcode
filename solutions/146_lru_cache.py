from collections import deque


def main():
    # 基本ケース
    lru = LRUCache(2)

    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1  # 1を返す

    lru.put(3, 3)           # 2を削除
    assert lru.get(2) == -1  # -1を返す（削除済み）

    lru.put(4, 4)           # 1を削除
    assert lru.get(1) == -1  # -1を返す（削除済み）
    assert lru.get(3) == 3  # 3を返す
    assert lru.get(4) == 4  # 4を返す

    # エッジケース - 容量1
    lru_small = LRUCache(1)
    lru_small.put(2, 1)
    assert lru_small.get(2) == 1
    lru_small.put(3, 2)
    assert lru_small.get(2) == -1
    assert lru_small.get(3) == 2

    print("All tests passed!")


class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


# Least Recently Used (LRU) Cache Implementation
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


class FIFOCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def get(self, key: int) -> int:
        return self.cache.get(key, -1)  # 順序は変更しない

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                oldest = self.order.popleft()
                del self.cache[oldest]

            self.cache[key] = value
            self.order.append(key)


if __name__ == '__main__':
    main()
