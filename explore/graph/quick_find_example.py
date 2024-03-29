# quick find
class UnionFind:
    def __init__(self, size) -> None:
        self.root = [i for i in range(size)]

    # O(1)
    def find(self, x):
        return self.root[x]

    # O(N)
    def union(self, x, y):
        rootX = self.root[x]
        rootY = self.root[y]

        if rootX != rootY:
            for i in range(0, len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.root[x] == self.root[y]


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)

print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true
