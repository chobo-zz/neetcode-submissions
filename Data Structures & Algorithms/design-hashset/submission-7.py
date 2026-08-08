class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.data = [ListNode(0) for i in range(100)]

    def add(self, key: int) -> None:
        index = key % len(self.data)
        cur = self.data[index]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.data)
        cur = self.data[index]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % len(self.data)
        cur = self.data[index]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)