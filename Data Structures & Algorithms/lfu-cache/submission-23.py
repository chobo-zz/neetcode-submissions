class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        self.left.next = self.right
        self.right.prev = self.left
    
    def pop(self, node):
        nodeBefore = node.prev
        nodeAfter = node.next

        nodeBefore.next = nodeAfter
        nodeAfter.prev = nodeBefore

        self.size -= 1
    
    def pushRight(self, node):
        nodeBefore = self.right.prev
        nodeBefore.next = node
        node.next = self.right

        self.right.prev = node
        node.prev = nodeBefore
        
        self.size += 1
    
    def popLeft(self):
        node = self.left.next
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size -= 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.nodeMap = defaultdict(Node) # key -> Node
        self.listMap = defaultdict(LinkedList) # freq -> LinkedList
        self.cap = capacity
        self.lfu = 1 # tracks current LFU count that contains valid Nodes

    def counter(self, node):
        self.listMap[node.freq].pop(node)

        if self.listMap[self.lfu].size == 0:
            self.lfu += 1
        
        node.freq += 1
        self.listMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return
            
        if len(self.nodeMap) >= self.cap:
            node = self.listMap[self.lfu].popLeft()
            del self.nodeMap[node.key]
            
        node = Node(key, value)
        self.nodeMap[key] = node
        self.lfu = 1
        self.listMap[self.lfu].pushRight(node)
        

        
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)