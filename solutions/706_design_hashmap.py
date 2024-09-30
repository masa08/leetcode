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
        bucket = self.table[index]

        # bucketに複数の値が入っている場合、
        # 該当する値を配列の先頭に移動し、pop(0)を実行
        # eg. index = 57, bucket = [[657, 790], [157, 493]]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                temp = bucket[i]
                bucket[i] = bucket[0]
                bucket[0] = temp
                bucket.pop(0)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
