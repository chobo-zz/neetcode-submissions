class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes = {} # cache that stores key -> Node
        self.capacity = capacity

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        nodeBefore = self.right.prev

        nodeBefore.next = node
        node.next = self.right

        self.right.prev = node
        node.prev = nodeBefore
    
    def remove(self, node):
        nodeBefore = node.prev
        nodeAfter = node.next

        nodeBefore.next = nodeAfter
        nodeAfter.prev = nodeBefore


    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]

        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.remove(self.nodes[key])


        node = Node(key, value)
        self.nodes[key] = node
        self.insert(node)

        if len(self.nodes) > self.capacity:
            nodeToEvict = self.left.next
            self.remove(nodeToEvict)
            del self.nodes[nodeToEvict.key]

        
        
        
