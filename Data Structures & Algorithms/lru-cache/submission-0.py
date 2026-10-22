class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev


    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        
        self.remove(self.m[key])
        self.insert(self.m[key])

        return self.m[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.remove(self.m[key])
        
        self.m[key] = Node(key, value)
        self.insert(self.m[key])
        
        if len(self.m) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.m[lru.key]

