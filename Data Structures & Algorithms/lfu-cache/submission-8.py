class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    
    def pop(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        self.size -= 1
    
    def pushRight(self, node):
        before = self.right.prev
        before.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = before
        self.size += 1
    
    def popLeft(self):
        node = self.left.next
        after = node.next
        self.left.next = self.left.next.next
        after.prev = self.left
        self.size -= 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = defaultdict(ListNode) # key -> node
        self.listMap = defaultdict(LinkedList) # freq -> linked list
        self.lfuCount = 0

    def counter(self, node):
        count = node.freq

        self.listMap[count].pop(node)

        if count == self.lfuCount and self.listMap[count].size == 0:
            self.lfuCount += 1
        
        node.freq += 1
        self.listMap[node.freq].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.counter(node)
            return
        
        if len(self.nodeMap) == self.capacity:
            node = self.listMap[self.lfuCount].popLeft()
            del self.nodeMap[node.key]
        
        node = ListNode(key, value)
        self.lfuCount = 1
        self.nodeMap[key] = node
        self.listMap[self.lfuCount].pushRight(node)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)