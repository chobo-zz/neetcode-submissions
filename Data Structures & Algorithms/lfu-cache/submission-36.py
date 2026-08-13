class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.count = 1
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
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
        self.left.next = node.next
        node.next.prev = self.left
        self.size -= 1
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.listMap = defaultdict(LinkedList) # frequency count -> linked list
        self.nodeMap = defaultdict(ListNode) # key -> node
        self.capacity = capacity
        self.lfuCount = 1

    def counter(self, node):
        curFreq = node.count
        self.listMap[curFreq].pop(node)

        if curFreq == self.lfuCount and self.listMap[self.lfuCount].size == 0:
            self.lfuCount += 1
        
        node.count += 1
        self.listMap[node.count].pushRight(node)
            

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        node = self.nodeMap[key]
        self.counter(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.counter(self.nodeMap[key])
            self.nodeMap[key].val = value
            return
        
        if self.capacity == len(self.nodeMap):
            node = self.listMap[self.lfuCount].popLeft()
            del self.nodeMap[node.key]
        
        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.lfuCount = 1
        self.listMap[self.lfuCount].pushRight(node)
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)