class MyHashMap:
    def __init__(self):
        self.size = 100
        self.table = [[] for _ in range(self.size)]

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def get(self, key: int) -> int:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        table = self.table[index]

        for i in range(len(table)):
            if table[i][0] == key:
                table[0], table[i] = table[i], table[0]
                table.pop(0)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
