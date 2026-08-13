class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.count = 1

class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        
        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0
    
    def pop(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        self.size -= 1
    
    def pushRight(self, node):
        before = self.right.prev
        before.next = node
        node.prev = before
        node.next = self.right
        self.right.prev = node
        self.size += 1
    
    def popLeft(self):
        after = self.left.next
        self.left.next = after.next
        after.next.prev = self.left
        self.size -= 1
        return after

class LFUCache:

    def __init__(self, capacity: int):
        self.nodeMap = defaultdict(ListNode)
        self.listMap = defaultdict(LinkedList)
        self.lfuCount = 1
        self.capacity = capacity

    def counter(self, node):
        count = node.count

        self.listMap[count].pop(node)

        if count == self.lfuCount and self.listMap[count].size == 0:
            self.lfuCount += 1
        
        node.count += 1
        self.listMap[node.count].pushRight(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.counter(node)
            node.value = value
            return
        
        if len(self.nodeMap) == self.capacity:
            nodeToRemove = self.listMap[self.lfuCount].popLeft()
            del self.nodeMap[nodeToRemove.key]
        
        self.lfuCount = 1
        nodeToAdd = ListNode(key, value)
        self.nodeMap[key] = nodeToAdd
        self.listMap[self.lfuCount].pushRight(nodeToAdd)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)