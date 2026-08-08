class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # { key: Node }
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.capacity = capacity

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = node
        node.next = next

        node.prev = prev
        next.prev = node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        # get node's val from cache
        # move that node to end of list (delete/insert)

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]
        
