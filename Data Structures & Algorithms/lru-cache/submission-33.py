class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key -> node, node contains value
        self.capacity = capacity

        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        nodeBeforeRight = self.right.prev

        nodeBeforeRight.next = node
        node.prev = nodeBeforeRight
        node.next = self.right
        self.right.prev = node
    
    def remove(self, node):
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            nodeAfterLeft = self.left.next
            self.remove(nodeAfterLeft)
            del self.cache[nodeAfterLeft.key]
        
        
