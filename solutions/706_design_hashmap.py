class MyHashMap:
    def __init__(self):
        self.size = 100
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key: int) -> int:
        index = self.hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        table = self.table[index]
        for i, (k, _) in enumerate(table):
            if k == key:
                table.pop(i)
                break


def main():
    # Test case 1: 基本操作
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    assert hashmap.get(1) == 1
    assert hashmap.get(3) == -1
    hashmap.put(2, 1)  # 更新
    assert hashmap.get(2) == 1
    hashmap.remove(2)
    assert hashmap.get(2) == -1
    print("Test case 1 passed ✓")

    # Test case 2: 衝突処理
    hashmap = MyHashMap()
    hashmap.put(1, 10)
    hashmap.put(101, 20)  # 1 と 101 は同じバケット（1 % 100 = 101 % 100 = 1）
    hashmap.put(201, 30)  # さらに衝突
    assert hashmap.get(1) == 10
    assert hashmap.get(101) == 20
    assert hashmap.get(201) == 30
    print("Test case 2 passed ✓")

    # Test case 3: 削除後の動作
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(101, 2)
    hashmap.put(201, 3)
    hashmap.remove(101)
    assert hashmap.get(1) == 1
    assert hashmap.get(101) == -1
    assert hashmap.get(201) == 3
    print("Test case 3 passed ✓")

    # Test case 4: 大量のデータ
    hashmap = MyHashMap()
    for i in range(1000):
        hashmap.put(i, i * 10)
    for i in range(1000):
        assert hashmap.get(i) == i * 10
    print("Test case 4 passed ✓")

    print("\nAll tests passed! 🎉")


if __name__ == "__main__":
    main()
