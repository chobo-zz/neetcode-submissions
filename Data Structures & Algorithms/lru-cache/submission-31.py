class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

        self.cache = {}
        self.capacity = capacity

    def insert(self, node):
        left = self.right.prev
        right = self.right

        node.next = right
        node.prev = left

        left.next = node
        right.prev = node
    
    def remove(self, node):
        left = node.prev
        right = node.next

        left.next = node.next
        right.prev = node.prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            nodeToRemove = self.left.next
            self.remove(nodeToRemove)
            del self.cache[nodeToRemove.key]
    
        
