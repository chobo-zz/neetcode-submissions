class Node:
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = defaultdict(Node) # key -> Node
        self.left = Node(-1, -1, None, None)
        self.right = Node(-1, -1, None, None)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):
        before = self.right.prev
        before.next = node
        node.prev = before
        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value, None, None)
        node = self.cache[key]
        self.insert(node)

        if len(self.cache) > self.capacity:
            after = self.left.next
            self.remove(after)
            del self.cache[after.key]
        
        
        
        
        
