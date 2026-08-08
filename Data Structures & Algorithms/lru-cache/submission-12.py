class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def insert(self, node: Node) -> None:
        prev = self.right.prev
        next = self.right

        node.next = next
        node.prev = prev

        prev.next = node
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        # need to also move retrieved key to end of list

        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        

        if len(self.cache) > self.capacity:
            # remove left-most node from linked list
            # delete key from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        
