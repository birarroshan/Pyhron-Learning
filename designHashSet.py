class MyHashSet:
    bsize=1231
    def __init__(self):
        self.bucket = [[] for _ in range(self.bsize)]

    def add(self, key: int) -> None:
        idx= key % self.bsize
        if key not in self.bucket[idx]:
            self.bucket[idx].append(key)

    def remove(self, key: int) -> None:
        idx= key % self.bsize
        if key in self.bucket[idx]:
            self.bucket[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx= key % self.bsize
        if key in self.bucket[idx]:
            return True
        else:
            return False

obj = MyHashSet()
obj.add(0)
obj.remove(1)
param_3 = obj.contains(10)