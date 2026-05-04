from typing import List
class MyHashMap:  

    ### can also be done with LinkedList

    bs = 9
    def __init__(self):
        self.hmap = [[] for _ in range(self.bs)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.bs
        for i,(k,v) in enumerate(self.hmap[idx]):
            if k == key:
                self.hmap[idx][i] = (k,value)
                return
        self.hmap[idx].append((key,value))
    
    def get(self, key: int) -> int:
        idx = key % self.bs
        for i,(k,v) in enumerate(self.hmap[idx]):
            if k == key:
                return v
        return -1
    
    def remove(self, key: int) -> None:
        idx = key % self.bs
        for i,(k,v) in enumerate(self.hmap[idx]):
            if k == key:
                self.hmap[idx].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)